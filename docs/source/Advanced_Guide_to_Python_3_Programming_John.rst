Advanced Guide to Python 3 Programming, John

1
Introduction .
1.1
Introduction .
Part I
1
1
Computer Graphics
2Introduction to Computer Graphics .
2.1
Introduction .
2.2
Background .
2.3
The Graphical Computer Era .
2.4
Interactive and Non Interactive Graphics .
2.5
Pixels .
2.6
Bit Map Versus Vector Graphics .
2.7
Buffering .
2.8
Python and Computer Graphics .
2.9
References .
2.10 Online Resources .5
3Python Turtle Graphics .
3.1
Introduction .
3.2
The Turtle Graphics Library .
3.2.1
The Turtle Module .
3.2.2
Basic Turtle Graphics .
3.2.3
Drawing Shapes .
3.2.4
Filling Shapes .
3.3
Other Graphics Libraries .
3.4
3D Graphics .
3.4.1
PyOpenGL .
3.5
Online Resources .
3.6
Exercises .13
Contents
4Computer Generated Art .
4.1
Creating Computer Art .
4.2
A Computer Art Generator .
4.3
Fractals in Python .
4.3.1
The Koch Snowﬂake .
4.3.2
Mandelbrot Set .
4.4
Online Resources .
4.5
Exercises .23
5Introduction to Matplotlib .
5.1
Introduction .
5.2
Matplotlib .
5.3
Plot Components .
5.4
Matplotlib Architecture .
5.4.1
Backend Layer .
5.4.2
The Artist Layer .
5.4.3
The Scripting Layer .
5.5
Online Resources .35
6Graphing with Matplotlib pyplot .
6.1
Introduction .
6.2
The pyplot API .
6.3
Line Graphs .
6.3.1
Coded Format Strings .
6.4
Scatter Graph .
6.4.1
When to Use Scatter Graphs .
6.5
Pie Charts .
6.5.1
Expanding Segments .
6.5.2
When to Use Pie Charts .
6.6
Bar Charts .
6.6.1
Horizontal Bar Charts .
6.6.2
Coloured Bars .
6.6.3
Stacked Bar Charts .
6.6.4
Grouped Bar Charts .
6.7
Figures and Subplots .
6.8
3D Graphs .
6.9
Exercises .43
7Graphical User Interfaces .
7.1
Introduction .
7.2
GUIs and WIMPS .67
67
68Contents
7.3
xv
Windowing Frameworks for Python .
7.3.1
Platform-Independent GUI Libraries .
7.3.2
Platform-Speciﬁc GUI Libraries .
Online Resources .69
70
70
71
8The wxPython GUI Library .
8.1
The wxPython Library .
8.1.1
wxPython Modules .
8.1.2
Windows as Objects .
8.1.3
A Simple Example .
8.2
The wx.App Class .
8.3
Window Classes .
8.4
Widget/Control Classes .
8.5
Dialogs .
8.6
Arranging Widgets Within a Container .
8.7
Drawing Graphics .
8.8
Online Resources .
8.9
Exercises .
8.9.1
Simple GUI Application .73
9Events in wxPython User Interfaces .
9.1
Event Handling .
9.2
Event Deﬁnitions .
9.3
Types of Events .
9.4
Binding an Event to an Event Handler .
9.5
Implementing Event Handling .
9.6
An Interactive wxPython GUI .
9.7
Online Resources .
9.8
Exercises .
9.8.1
Simple GUI Application .
9.8.2
GUI Interface to a Tic Tac Toe Game .87
10 PyDraw wxPython Example Application .
10.1 Introduction .
10.2 The PyDraw Application .
10.3 The Structure of the Application .
10.3.1 Model, View and Controller Architecture .
10.3.2 PyDraw MVC Architecture .
10.3.3 Additional Classes .
10.3.4 Object Relationships .
10.4 The Interactions Between Objects .
10.4.1 The PyDrawApp .
10.4.2 The PyDrawFrame Constructor .99
7.4xvi
Contents
10.5
10.6
10.7
Part II
10.4.3 Changing the Application Mode .
10.4.4 Adding a Graphic Object .
The Classes .
10.5.1 The PyDrawConstants Class .
10.5.2 The PyDrawFrame Class .
10.5.3 The PyDrawMenuBar Class .
10.5.4 The PyDrawToolBar Class .
10.5.5 The PyDrawController Class .
10.5.6 The DrawingModel Class .
10.5.7 The DrawingPanel Class .
10.5.8 The DrawingController Class .
10.5.9 The Figure Class .
10.5.10 The Square Class .
10.5.11 The Circle Class .
10.5.12 The Line Class .
10.5.13 The Text Class .
References .
Exercises .
Computer Games
11 Introduction to Games Programming .
11.1 Introduction .
11.2 Games Frameworks and Libraries .
11.3 Python Games Development .
11.4 Using Pygame .
11.5 Online Resources .121
12 Building Games with pygame .
12.1 Introduction .
12.2 The Display Surface .
12.3 Events .
12.3.1 Event Types .
12.3.2 Event Information .
12.3.3 The Event Queue .
12.4 A First pygame Application .
12.5 Further Concepts .
12.6 A More Interactive pygame Application .
12.7 Alternative Approach to Processing Input Devices .
12.8 pygame Modules .
12.9 Online Resources .125
13 StarshipMeteors pygame .
13.1 Creating a Spaceship Game .
13.2 The Main Game Class .
13.3 The GameObject Class .
13.4 Displaying the Starship .
13.5 Moving the Spaceship .
13.6 Adding a Meteor Class .
13.7 Moving the Meteors .
13.8 Identifying a Collision .
13.9 Identifying a Win .
13.10 Increasing the Number of Meteors .
13.11 Pausing the Game .
13.12 Displaying the Game Over Message .
13.13 The StarshipMeteors Game .
13.14 Online Resources .
13.15 Exercises .141
Testing
14 Introduction to Testing .
14.1 Introduction .
14.2 Types of Testing .
14.3 What Should Be Tested? .
14.4 Testing Software Systems .
14.4.1 Unit Testing .
14.4.2 Integration Testing .
14.4.3 System Testing .
14.4.4 Installation/Upgrade Testing .
14.4.5 Smoke Tests .
14.5 Automating Testing .
14.6 Test Driven Development .
14.6.1 The TDD Cycle .
14.6.2 Test Complexity .
14.6.3 Refactoring .
14.7 Design for Testability .
14.7.1 Testability Rules of Thumb .
14.8 Online Resources .
14.9 Book Resources .165
15 PyTest Testing Framework .
15.1 Introduction .
15.2 What Is PyTest? .
15.3 Setting Up PyTest .
15.4 A Simple PyTest Example .175
175
175
176
176xviii
Contents
15.5
15.6
15.7
15.8
Working with PyTest .
Parameterised Tests .
Online Resources .
Exercises .179
183
185
185
16 Mocking for Testing .
16.1 Introduction .
16.2 Why Mock? .
16.3 What Is Mocking? .
16.4 Common Mocking Framework Concepts .
16.5 Mocking Frameworks for Python .
16.6 The unittest.mock Library .
16.6.1 Mock and Magic Mock Classes .
16.6.2 The Patchers .
16.6.3 Mocking Returned Objects .
16.6.4 Validating Mocks Have Been Called .
16.7 Mock and MagicMock Usage .
16.7.1 Naming Your Mocks .
16.7.2 Mock Classes .
16.7.3 Attributes on Mock Classes .
16.7.4 Mocking Constants .
16.7.5 Mocking Properties .
16.7.6 Raising Exceptions with Mocks .
16.7.7 Applying Patch to Every Test Method .
16.7.8 Using Patch as a Context Manager .
16.8 Mock Where You Use It .
16.9 Patch Order Issues .
16.10 How Many Mocks? .
16.11 Mocking Considerations .
16.12 Online Resources .
16.13 Exercises .187
Part IV
File Input/Output
17 Introduction to Files, Paths and IO .
17.1 Introduction .
17.2 File Attributes .
17.3 Paths .
17.4 File Input/Output .
17.5 Sequential Access Versus Random Access .
17.6 Files and I/O in Python .
17.7 Online Resources .
214Contentsxix
18 Reading and Writing Files .
18.1 Introduction .
18.2 Obtaining References to Files .
18.3 Reading Files .
18.4 File Contents Iteration .
18.5 Writing Data to Files .
18.6 Using Files and with Statements .
18.7 The Fileinput Module .
18.8 Renaming Files .
18.9 Deleting Files .
18.10 Random Access Files .
18.11 Directories .
18.12 Temporary Files .
18.13 Working with Paths .
18.14 Online Resources .
18.15 Exercise .215
19 Stream IO .
19.1 Introduction .
19.2 What is a Stream? .
19.3 Python Streams .
19.4 IOBase .
19.5 Raw IO/UnBuffered IO Classes .
19.6 Binary IO/Buffered IO Classes .
19.7 Text Stream Classes .
19.8 Stream Properties .
19.9 Closing Streams .
19.10 Returning to the open() Function .
19.11 Online Resources .
19.12 Exercise .231
20 Working with CSV Files .
20.1 Introduction .
20.2 CSV Files .
20.2.1 The CSV Writer Class .
20.2.2 The CSV Reader Class .
20.2.3 The CSV DictWriter Class .
20.2.4 The CSV DictReader Class .
20.3 Online Resources .
20.4 Exercises .241
21 Working with Excel Files 249
21.1 Introduction 249
21.2 Excel Files 249xx
Contents
The OpenpyxlWorkbook Class .
The OpenpyxlWorkSheet Objects .
Working with Cells .
Sample Excel File Creation Application .
Loading a Workbook from an Excel File .
Online Resources .
Exercises .250
22 Regular Expressions in Python .
22.1 Introduction .
22.2 What Are Regular Expressions? .
22.3 Regular Expression Patterns .
22.3.1 Pattern Metacharacters .
22.3.2 Special Sequences .
22.3.3 Sets .
22.4 The Python re Module .
22.5 Working with Python Regular Expressions .
22.5.1 Using Raw Strings .
22.5.2 Simple Example .
22.5.3 The Match Object .
22.5.4 The search() Function .
22.5.5 The match() Function .
22.5.6 The Difference Between Matching and Searching .
22.5.7 The ﬁndall() Function .
22.5.8 The ﬁnditer() Function .
22.5.9 The split() Function .
22.5.10 The sub() Function .
22.5.11 The compile() Function .
22.6 Online Resources .
22.7 Exercises .257
Part V
Database Access
23 Introduction to Databases .
23.1 Introduction .
23.2 What Is a Database? .
23.2.1 Data Relationships .
23.2.2 The Database Schema .
23.3 SQL and Databases .
23.4 Data Manipulation Language .
23.5 Transactions in Databases .
23.6 Further Reading .
282Contentsxxi
24 Python DB-API .
24.1 Accessing a Database from Python .
24.2 The DB-API .
24.2.1 The Connect Function .
24.2.2 The Connection Object .
24.2.3 The Cursor Object .
24.2.4 Mappings from Database Types to Python Types .
24.2.5 Generating Errors .
24.2.6 Row Descriptions .
24.3 Transactions in PyMySQL .
24.4 Online Resources .283
25 PyMySQL Module .
25.1 The PyMySQL Module .
25.2 Working with the PyMySQL Module .
25.2.1 Importing the Module .
25.2.2 Connect to the Database .
25.2.3 Obtaining the Cursor Object .
25.2.4 Using the Cursor Object .
25.2.5 Obtaining Information About the Results .
25.2.6 Fetching Results .
25.2.7 Close the Connection .
25.3 Complete PyMySQL Query Example .
25.4 Inserting Data to the Database .
25.5 Updating Data in the Database .
25.6 Deleting Data in the Database .
25.7 Creating Tables .
25.8 Online Resources .
25.9 Exercises .291
Part VI
Logging
26 Introduction to Logging .
26.1 Introduction .
26.2 Why Log? .
26.3 What Is the Purpose of Logging? .
26.4 What Should You Log? .
26.5 What Not to Log .
26.6 Why Not Just Use Print? .
26.7 Online Resources .
27 Logging in Python 311
27.1 The Logging Module 311
27.2 The Logger 312xxii
Contents
Controlling the Amount of Information Logged .
Logger Methods .
Default Logger .
Module Level Loggers .
Logger Hierarchy .
Formatters .
27.8.1 Formatting Log Messages .
27.8.2 Formatting Log Output .
27.9 Online Resources .
27.10 Exercises .313
28 Advanced Logging .
28.1 Introduction .
28.2 Handlers .
28.2.1 Setting the Root Output Handler .
28.2.2 Programmatically Setting the Handler .
28.2.3 Multiple Handlers .
28.3 Filters .
28.4 Logger Conﬁguration .
28.5 Performance Considerations .
28.6 Exercises .323
Part VII
Concurrency and Parallelism
29 Introduction to Concurrency and Parallelism .
29.1 Introduction .
29.2 Concurrency .
29.3 Parallelism .
29.4 Distribution .
29.5 Grid Computing .
29.6 Concurrency and Synchronisation .
29.7 Object Orientation and Concurrency .
29.8 Threads V Processes .
29.9 Some Terminology .
29.10 Online Resources .337
30 Threading .
30.1 Introduction .
30.2 Threads .
30.3 Thread States .
30.4 Creating a Thread .
30.5 Instantiating the Thread Class .
30.6 The Thread Class .347
347
347
347
348
349
350Contents
30.7
30.8
30.9
30.10
30.11
30.12
30.13
30.14
30.15
30.16
xxiii
The Threading Module Functions .
Passing Arguments to a Thread .
Extending the Thread Class .
Daemon Threads .
Naming Threads .
Thread Local Data .
Timers .
The Global Interpreter Lock .
Online Resources .
Exercise .352
352
354
355
356
357
358
359
360
360
31 Multiprocessing .
31.1 Introduction .
31.2 The Process Class .
31.3 Working with the Process Class .
31.4 Alternative Ways to Start a Process .
31.5 Using a Pool .
31.6 Exchanging Data Between Processes .
31.7 Sharing State Between Processes .
31.7.1 Process Shared Memory .
31.8 Online Resources .
31.9 Exercises .363
363
363
365
366
368
372
374
374
375
376
32 Inter Thread/Process Synchronisation .
32.1 Introduction .
32.2 Using a Barrier .
32.3 Event Signalling .
32.4 Synchronising Concurrent Code .
32.5 Python Locks .
32.6 Python Conditions .
32.7 Python Semaphores .
32.8 The Concurrent Queue Class .
32.9 Online Resources .
32.10 Exercises .377
377
377
380
382
383
386
388
389
391
391
33 Futures .
33.1 Introduction .
33.2 The Need for a Future .
33.3 Futures in Python .
33.3.1 Future Creation .
33.3.2 Simple Example Future .
33.4 Running Multiple Futures .
33.4.1 Waiting for All Futures to Complete .
33.4.2 Processing Results as Completed .395
395
395
396
397
397
399
400
402xxiv
Contents
33.5
33.6
33.7
Processing Future Results Using a Callback 403
Online Resources 405
Exercises 405
34 Concurrency with AsyncIO .
34.1 Introduction .
34.2 Asynchronous IO .
34.3 Async IO Event Loop .
34.4 The Async and Await Keywords .
34.4.1 Using Async and Await .
34.5 Async IO Tasks .
34.6 Running Multiple Tasks .
34.6.1 Collating Results from Multiple Tasks .
34.6.2 Handling Task Results as They Are Made
Available .
34.7 Online Resources .
34.8 Exercises .
Part VIII
407
407
407
408
409
409
411
414
414
415
416
417
Reactive Programming
35 Reactive Programming Introduction .
35.1 Introduction .
35.2 What Is a Reactive Application? .
35.3 The ReactiveX Project .
35.4 The Observer Pattern .
35.5 Hot and Cold Observables .
35.5.1 Cold Observables .
35.5.2 Hot Observables .
35.5.3 Implications of Hot and Cold Observables .
35.6 Differences Between Event Driven Programming and
Reactive Programming .
35.7 Advantages of Reactive Programming .
35.8 Disadvantages of Reactive Programming .
35.9 The RxPy Reactive Programming Framework .
35.10 Online Resources .
35.11 Reference .421
421
421
422
422
423
424
424
424
36 RxPy Observables, Observers and Subjects .
36.1 Introduction .
36.2 Observables in RxPy .
36.3 Observers in RxPy .
36.4 Multiple Subscribers/Observers .
36.5 Subjects in RxPy .429
429
429
430
432
433
425
425
426
426
426
427Contents
36.6
xxv
Observer Concurrency .
36.6.1 Available Schedulers .
Online Resources .
Exercises .435
437
438
438
37 RxPy Operators .
37.1 Introduction .
37.2 Reactive Programming Operators .
37.3 Piping Operators .
37.4 Creational Operators .
37.5 Transformational Operators .
37.6 Combinatorial Operators .
37.7 Filtering Operators .
37.8 Mathematical Operators .
37.9 Chaining Operators .
37.10 Online Resources .
37.11 Exercises .439
439
439
440
441
441
443
444
445
446
448
448
36.7
36.8
Part IX
Network Programming
38 Introduction to Sockets and Web Services .
38.1 Introduction .
38.2 Sockets .
38.3 Web Services .
38.4 Addressing Services .
38.5 Localhost .
38.6 Port Numbers .
38.7 IPv4 Versus IPv6 .
38.8 Sockets and Web Services in Python .
38.9 Online Resources .451
451
451
452
452
453
454
455
455
456
39 Sockets in Python .
39.1 Introduction .
39.2 Socket to Socket Communication .
39.3 Setting Up a Connection .
39.4 An Example Client Server Application .
39.4.1 The System Structure .
39.4.2 Implementing the Server Application .
39.5 Socket Types and Domains .
39.6 Implementing the Client Application .
39.7 The Socketserver Module .
39.8 HTTP Server .
39.9 Online Resources .
39.10 Exercises .457
457
457
458
458
458
459
461
461
463
465
469
469xxvi
Contents
40 Web Services in Python .
40.1 Introduction .
40.2 RESTful Services .
40.3 A RESTful API .
40.4 Python Web Frameworks .
40.5 Flask .
40.6 Hello World in Flask .
40.6.1 Using JSON .
40.6.2 Implementing a Flask Web Service .
40.6.3 A Simple Service .
40.6.4 Providing Routing Information .
40.6.5 Running the Service .
40.6.6 Invoking the Service .
40.6.7 The Final Solution .
40.7 Online Resources .471
471
471
472
473
474
474
474
475
475
476
477
478
479
479
41 Bookshop Web Service .
41.1 Building a Flask Bookshop Service .
41.2 The Design .
41.3 The Domain Model .
41.4 Encoding Books Into JSON .
41.5 Setting Up the GET Services .
41.6 Deleting a Book .
41.7 Adding a New Book .
41.8 Updating a Book .
41.9 What Happens if We Get It Wrong? .
41.10 Bookshop Services Listing .
41.11 Exercises .481
