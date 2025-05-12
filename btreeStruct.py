from collections import OrderedDict

BLOCK_SIZE = 512
NODE_DEGREE = 10
MAX_KEYS = 2 * NODE_DEGREE - 1  # 19
MAX_CHILDREN = 2 * NODE_DEGREE  # 20

class BTreeNode:
    def __init__(self, block_id, parent_id=0, is_leaf=True):
        self.block_id = block_id             # ID of this block
        self.parent_id = parent_id           # ID of the parent node
        self.is_leaf = is_leaf               # True if no children
        self.num_keys = 0                    # number of used keys

        self.keys = [0] * MAX_KEYS           # up to 19 keys
        self.values = [0] * MAX_KEYS         # up to 19 values
        self.children = [0] * MAX_CHILDREN   # up to 20 child block IDs

        self.dirty = True                    # if node needs to be flushed

    def to_bytes(self):
        data = bytearray(BLOCK_SIZE)
        offset = 0

        data[offset:offset+8] = self.block_id.to_bytes(8, 'big')
        offset += 8
        data[offset:offset+8] = self.parent_id.to_bytes(8, 'big')
        offset += 8
        data[offset:offset+8] = self.num_keys.to_bytes(8, 'big')
        offset += 8

        for i in range(MAX_KEYS):
            data[offset:offset+8] = self.keys[i].to_bytes(8, 'big')
            offset += 8
        for i in range(MAX_KEYS):
            data[offset:offset+8] = self.values[i].to_bytes(8, 'big')
            offset += 8
        for i in range(MAX_CHILDREN):
            data[offset:offset+8] = self.children[i].to_bytes(8, 'big')
            offset += 8

        return data

    @staticmethod
    def from_bytes(data):
        offset = 0

        block_id = int.from_bytes(data[offset:offset+8], 'big')
        offset += 8
        parent_id = int.from_bytes(data[offset:offset+8], 'big')
        offset += 8
        num_keys = int.from_bytes(data[offset:offset+8], 'big')
        offset += 8

        keys = [int.from_bytes(data[offset + i*8:offset + (i+1)*8], 'big') for i in range(MAX_KEYS)]
        offset += MAX_KEYS * 8
        values = [int.from_bytes(data[offset + i*8:offset + (i+1)*8], 'big') for i in range(MAX_KEYS)]
        offset += MAX_KEYS * 8
        children = [int.from_bytes(data[offset + i*8:offset + (i+1)*8], 'big') for i in range(MAX_CHILDREN)]

        node = BTreeNode(block_id, parent_id)
        node.num_keys = num_keys
        node.keys = keys
        node.values = values
        node.children = children
        node.is_leaf = (children[0] == 0)
        node.dirty = False
        return node


        
class BTree:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, 'r+b')
        self.cache = OrderedDict()

        self.root_id = self._read_root_id()
        if self.root_id == 0:
            self.root_id = 1
            self._write_root_id(self.root_id)
            root = BTreeNode(self.root_id)
            self._write_node(root)
            self._set_next_block_id(2)

    def _read_root_id(self):
        self.file.seek(8)
        return int.from_bytes(self.file.read(8), 'big')

    def _write_root_id(self, block_id):
        self.file.seek(8)
        self.file.write(block_id.to_bytes(8, 'big'))

    def _get_next_block_id(self):
        self.file.seek(16)
        return int.from_bytes(self.file.read(8), 'big')

    def _set_next_block_id(self, next_id):
        self.file.seek(16)
        self.file.write(next_id.to_bytes(8, 'big'))

    def _read_node(self, block_id):
        if block_id in self.cache:
            return self.cache[block_id]

        if len(self.cache) >= 3:
            self._evict_node()

        self.file.seek(block_id * BLOCK_SIZE)
        data = self.file.read(BLOCK_SIZE)
        node = BTreeNode.from_bytes(data)
        self.cache[block_id] = node
        return node

    def _write_node(self, node):
        self.file.seek(node.block_id * BLOCK_SIZE)
        self.file.write(node.to_bytes())
        node.dirty = False
        self.cache[node.block_id] = node

    def _evict_node(self):
        block_id, node = self.cache.popitem(last=False)
        if node.dirty:
            self._write_node(node)

    def insert(self, key, value):
        root = self._read_node(self.root_id)
        if root.num_keys == MAX_KEYS:
            new_root_id = self._get_next_block_id()
            self._set_next_block_id(new_root_id + 1)
            new_root = BTreeNode(new_root_id, is_leaf=False)
            new_root.children[0] = root.block_id
            self._split_child(new_root, 0, root)
            self.root_id = new_root.block_id
            self._write_root_id(self.root_id)
            self._insert_non_full(new_root, key, value)
        else:
            self._insert_non_full(root, key, value)

    def _insert_non_full(self, node, key, value):
        i = node.num_keys - 1

        # Check for duplicate key in current node
        for j in range(node.num_keys):
            if node.keys[j] == key:
                print(f"Key {key} already exists in the index.")
                return  # Reject the insert

        if node.children[0] == 0:  # Leaf node
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                node.values[i + 1] = node.values[i]
                i -= 1
            node.keys[i + 1] = key
            node.values[i + 1] = value
            node.num_keys += 1
            node.dirty = True
            
            print(f"Inserted key={key}, value={value} into '{filename}'.")
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            child = self._read_node(node.children[i])
            if child.num_keys == MAX_KEYS:
                self._split_child(node, i, child)
                if key > node.keys[i]:
                    i += 1
                child = self._read_node(node.children[i])
            self._insert_non_full(child, key, value)


    def _split_child(self, parent, i, child):
        new_block_id = self._get_next_block_id()
        self._set_next_block_id(new_block_id + 1)
        new_node = BTreeNode(new_block_id, parent_id=parent.block_id, is_leaf=child.children[0] == 0)

        mid = NODE_DEGREE - 1
        new_node.num_keys = NODE_DEGREE - 1

        new_node.keys[:mid] = child.keys[mid+1:MAX_KEYS]
        new_node.values[:mid] = child.values[mid+1:MAX_KEYS]
        if child.children[0] != 0:
            new_node.children[:NODE_DEGREE] = child.children[NODE_DEGREE:MAX_CHILDREN]

        child.num_keys = NODE_DEGREE - 1

        for j in range(parent.num_keys, i, -1):
            parent.children[j + 1] = parent.children[j]
            parent.keys[j] = parent.keys[j - 1]
            parent.values[j] = parent.values[j - 1]

        parent.children[i + 1] = new_node.block_id
        parent.keys[i] = child.keys[mid]
        parent.values[i] = child.values[mid]
        parent.num_keys += 1

        parent.dirty = True
        child.dirty = True
        new_node.dirty = True

        self._write_node(child)
        self._write_node(new_node)
        self._write_node(parent)

    def search(self, key):
        return self._search_node(self._read_node(self.root_id), key)

    def _search_node(self, node, key):
        i = 0
        while i < node.num_keys and key > node.keys[i]:
            i += 1
        if i < node.num_keys and key == node.keys[i]:
            return node.values[i]
        elif node.children[0] == 0:
            return None
        else:
            return self._search_node(self._read_node(node.children[i]), key)

    def traverse(self):
        yield from self._traverse_node(self._read_node(self.root_id))

    def _traverse_node(self, node):
        for i in range(node.num_keys):
            if node.children[i] != 0:
                yield from self._traverse_node(self._read_node(node.children[i]))
            yield (node.keys[i], node.values[i])
        if node.children[node.num_keys] != 0:
            yield from self._traverse_node(self._read_node(node.children[node.num_keys]))

    def close(self):
        for node in self.cache.values():
            if node.dirty:
                self._write_node(node)
        self.file.close()
