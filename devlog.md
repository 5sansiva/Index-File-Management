4/28/2025 3:11 PM
So my understanding for this project is that I will be making an interactive program that creates and manages index files. Those index files will contain a B tree. For this project, I am going to implement this project in python. It will be interactive in the sense that the user can input various commands as arguments which performs operations on an index file that is represented by the B tree. I understand that this project will be implemented in one file which is the index file whihc contains all the operations to perform and such. So far, this is my understanding, I shall read more and decide on how to structure my project in another session.
End session - 3:15 PM

5/3/2025 11:43 PM
So from before to this session, I haven't thought of anything new in terms of the project with overall development and such. I still probably want to read more and then start working on some basic stuff for the project to really get the gears grinding. This session, I plan on laying out the structure, and user interaction for this project with the command line prompts and such and see where I can go from there. Nothing too crazy or strict in terms of goals, just getting a feel for the project overall.

12:07 AM
So far, I am still trying to figure out how the structure should go. Because it is within a B tree, like do I create files which store B trees and all these commands essentially find files and such and perform stuff with that. It is rather confusing but it shouldn't be too bad.

12:17 AM
I have added the code for command input and then filled out the fileManager class. Now I have to add some speciics to that class and adjust.

End session - 12:18 AM - 5/4/2025
So for this session, it was mainly to just lay out a basic structure and understand what this project was going to be about. Now I understand that it is a file management system and that I will manage a bunch of index files and each files contains information stored in a B tree. It is pretty easy to think about but for some reason it was weird for me to think about when reading it so I get it now. Didn't have any major issues with the project so far so should be fine. Next session, I will go through each of the commands and get them working, mainly focusing on the create command.

Start session 5/4/2025 - 8:28 PM
From before, I have a better understanding on how the project is supposed to be. It has to include a B tree in each index file and certain actions have to be made from that. This session, I plan to work on the create choice that the user has for files and also make the B tree class and such.

9:23 PM
So far I am seeing how the index file will need to be created and such and how the storage works. It is still a bit confusing but nothing too bad.

10:28 PM
Went to go eat dinner so break

10:45 PM
So I updated to include the index file sizes and such. Still kinda confused on how it is supposed to be with memory so I am looking into that more.

End session 11:04 PM 5/4/2025
So for this session. I ended up finishing the create function. I haven't tested it yet and I am still wondering how the memory stuff needs to be managed so I will be working slowly towards that. Next sesssion I plan on finishing more of the commands and just get a better understanding and such.

Start session 12:02 AM 5/10/2025
So for this session, I haven't had many new thoughts on the project as I was dealing with other exams and work so I haven't been thinking about the project as much but I get the premise of the project so it hasn't been bad. This session, I look to finish that create function while detailing my work thoughout this sesssion.

12:57
Went through all the methods in the main and have filled those out. Now its to adjust the arugment becuase I can't use standard input.

1:07 AM End Session 5/10/2025
So this session wasn't anything much. I already got an idea for how to do the main method so I just finished that today. It is late so I haven't provided much detail. In my coming logs, I can provide much more. I need to start doing the b tree file and then connect these files together. That is my future goal.

9:53 AM - 5/10/2025
So just woke up and I am beginning to pick up from where I left off yesterday which is to finish the Btree class. This session I wil finish the Btree class and then see how to connect and test the flow of the program during execution.

11:04 AM
Had to go eat breakfast before. I did the Btree class. Need to do the Btree node.

11:40 PM - 5/10/2025 - End session
I stopped working, I forgot to log it. So this session I finished the main webpage and I also worked on the btree file and I finished the Btree file and each commands. I believe I need a BTree node so I might have to add that as well. Next session, is to go through testing and there will be some specifics with that. I haven't really tested my code when coding so I will need to edit that.

7:02 PM - 5/10/2025 Start Session
Ok so from last sesssion, I didn't really think of anything. I will continue working from where I left of which is on the BTree file, so finishing up the Btree and the node for the Btree. I do not have any more real faults in my understanding, besides maybe the memory aspect of the assignment as organizing each node in memory might be a bit of a tricky part but it shouldn't be too bad.

8:15 PM
So I was working but kinda got distracted just reading the textbook and such so I will lock back in.

8:32 PM
So I was going over the previous header information and such and how to organize it and the nodes and such.

8:46 PM
Ok so I think I am done with the btree.py method. I added the Btree node method along with the overall Btree method.

9:03 PM
When I am running this file, the create is working properly as a new test.idx has been created but when I try and insert a file with a key and value pair, it isn't working. There is an issue that keeps saying that the insert only takes in 2 positional arugments which is how I set it up but 3 were given yet I do not know how that is possible.

10-11 PM
I took a break in between to go eat dinner and such. I am still stuck on that issue.

11:15 PM
So I figured out that other issue from before, I essentially changed where I inserted part of btree.insert(key, value) to be btree.insert(key = key, value = value). Its a small issue and I just found that online as a potential fix for arugment issues so I decided to do it and it ended up working.

11:25 PM
So the testing inserts properly but it is not printing properly so I have to take a look at that and see there the issue might be.

11:45 PM
So I found out that the inserts might not being inserting properly as when I inputted the .idx file, it should have worked but it didn't and there were just nulls so I have to fix that now. Also, the print isn't working and such.

12:00 PM
Ok so I ended up adding the line btree.close() after inserting which ended up fixing that issue.

12:37 PM 5/11/2025 End Session
Alright so from this session, I was able to test my program and I ended up fixing a couple minor issues when it comes to arguments along with overall performance of the tool including printing, and inserting keys and values into the system. Next session, I will probably work on general user flow to make sure everything goes smoothly and try and perform fuzzing so everything works for this project. I should probably be done and ready to turn in after next work session.

8:06 PM 5/11/2025 Start session
Alright so from last session, I got the program working and such. Now today I am just going to perform testing to make sure that this is running properly and such. I will probably submit at the end of this session.
