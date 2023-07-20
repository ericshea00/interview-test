# Interview Project
## Premise
You are making an application that will allow users to post messages that get saved to a file and then for other users
to read those messages, edit them and save them back to the file. The plan is to eventually support thousands of users
and millions of messages being edited and modified. Any message should only be edited by a single user at a time. The
contents of the messages are to be saved to files by design and will not change in the future.


## Assignment
- Plan on spending approximately **four hours** on this project.
- Determine what is feasible to complete in that time frame.
- Create a list of tasks that you would need to complete to get the application to a working state that cannot be completed in the time frame.
- Review the code and implement the most important features that you can in the time frame with a prioritization
  on implementing code that will grow with the application.
- The goal is not so much to get the code functioning as much as it is to demonstrate your thought process and
  how you would approach the problem with actual code written demonstrating how you structure your code.

## Other Considerations
- Given that the initial iteration is using local files, consider implementing a file handler that will grow with the application
and work with cloud services in the future.
- How should the application handle concurrency? What changes to the database model needs to happen?


# Solution

## Questions
- Why are we even deleting the files or database records. In the current implementation we don't have any historic view of these messages.

## Assignment
1) Update application to allow for editing/updating messages (PUT).
2) Restructure code to separate responsiblities for file handling, database interations, etc.
3) Get a message by id rather than having to read though messages or deleting
4) Delete message without reading the next message(s).

## Outside scope:
1) Permissioning around editing/reading messages. Maybe certain users should only read/edit certain messages.
2) Testing for endpoints, resources, services, and db model.
3) More elegant validation and error handling.
4) Authentication
5) Max content/file size handling. Many many files could take up disk space and cause issues.
6) Documentation with examples of house to use the API
7) Feature for basic locking on messages when updating to only allow 1 user editing at a time.
8) Fields in database model to track additional data (author, locked, last_modified, timestamp).
9) Fields in database model to track additional data (author, locked, last_modified, timestamp).

## Concurrency
- Methods of locking would assist with concurrency concerns. 
- Using version numbers or timestamps could be another approach.

