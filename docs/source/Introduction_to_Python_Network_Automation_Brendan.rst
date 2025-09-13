Introduction to Python Network Automation, Brendan Choi
======================================================

1: Introduction to Python Network Automation␈ 1
--------------------------------------------

Laying the Foundation␈ 1
Exploring Your Skills and Prerequisites␈ 2
General Competencies of Three Main IT Domain Group␈ 3
Comparative Analysis of IT Engineers’ Responsibilities␈ 6
Python and Network Automation Studies␈ 10
Why Do People Want to Learn Python?␈ 10
What Do I Need to Study Network Automation Using Python?␈ 12
Hardware: Minimum Specifications for Laptop or PC␈ 13
Software Requirements␈ 14
Building a Network Automation Development Environment Using GNS3␈ 16
Downloading Supplementary Guides and Source Code␈ 20
Summary␈ 21
Storytime 1: Mega Speed Shoe Factory␈ 21
v■ Table of Contents
■Chapter
■
2: Learn Python Basics on Windows␈ 23
----------------------------------

“Hello, World!” and print( ) Function in Interactive Mode␈ 24
Preparing for the Python Exercises␈ 27
Understanding Data Types␈ 28
Indentation and Code Blocks␈ 30
Commenting␈ 31
Python Naming Convention␈ 32
Doing the Python Exercises␈ 33
Variables and Strings␈ 34
Exercise 2-1: Create Variables and Assign Various Data Types␈ 34
Exercise 2-2: Create Variables and Use the print( ) Function to Print Output␈ 35
Exercise 2-3: Use Abbreviated Variable Assignment␈ 36
Exercise 2-4: Enter a String, Escape Character Backslash (\), and type( ) Function␈ 36
Exercise 2-5: Determine If a Variable Is a Container, a Tag, or a Pointer␈ 38
Exercise 2-6: Use String Indexing␈ 39
Exercise 2-7: Understand Variable Assignment Errors␈ 39
Exercise 2-8: Avoid “SyntaxError: EOL While Scanning String Literal”␈ 40
Exercise 2-9: Avoid “NameError: name ‘variable_name’ is not defined”␈ 40
Exercise 2-10: Avoid “SyntaxError: invalid syntax”␈ 41
Exercise 2-11: Avoid “TypeError: ‘str’ object is not callable”␈ 41
Exercise 2-12: Add Multiline Comments with Triple Quotation Marks␈ 43
Exercise 2-13: Use \ as an Escape Character to Remove Special Character Meanings␈ 44
Exercise 2-14: Enter (Inject) Values/Strings in a String Using %s␈ 44
Printing, Concatenating, and Converting Strings␈ 45
Exercise 2-15: Use the print( ) and len( ) Functions to Create a Simple Function␈ 45
Exercise 2-16: Use the lower( ) and upper( ) String Methods␈ 46
Exercise 2-17: Perform String Concatenation and Use the str( ) Method␈ 46
Exercise 2-18: Learn to Change a String Using Curly Brackets and .format( )␈ 47
Exercise 2-19: Adjust the Text Position with Curly Brackets and .format( )␈ 48
Exercise 2-20: Adjust the Number of Decimal Places␈ 49
Exercise 2-21: Ask for and Receive User Input with input( )␈ 49
Exercise 2-22: Change a Word or Characters in a String␈ 50
Recap: Variables and Strings␈ 51
Numbers and Arithmetic Operators␈ 52
Exercise 2-23: Use Arithmetic Operators␈ 52
Exercise 2-24: Understand Integers vs. Strings␈ 53
Recap: Arithmetic Operators␈ 53
Booleans and Relational Operators␈ 54
Exercise 2-25: Use Booleans␈ 54
Exercise 2-26: Use Relational Operators␈ 55
Exercise 2-27: Use Boolean Expressions to Test True or False␈ 55
Exercise 2-28: Use Logical (Membership) Operators␈ 56
Exercise 2-29: Change the Order of Operation with ( )␈ 56
Control Statements: if, elif, and else␈ 56
Exercise 2-30: Use if and else␈ 57
Exercise 2-31: Use if, elif, and else␈ 57
Exercise 2-32: Write Code with if, elif, and else␈ 58
Recap: Boolean and Conditionals␈ 59
Functions␈ 59
Exercise 2-33: Defining a Function␈ 60
Exercise 2-34: Assign Default Values to a Function␈ 60
Exercise 2-35: Define Hello and Goodbye Functions␈ 61
Exercise 2-36: Use the Odd or Even Function␈ 62
Exercise 2-37: Nest a Function Within a Function␈ 62
Recap: Functions␈ 63
Lists␈ 63
Exercise 2-38: Create a List and Index Items␈ 63
Exercise 2-39: Use append, extend, and insert in a List␈ 64
Slicing␈ 65
Exercise 2-40: Slice a List␈ 65
vii■ Table of Contents
Exceptions and Error Handling␈ 66
Exercise 2-41: Avoid a ValueError Error␈ 66
Exercise 2-42: Handle Errors with try and except in a List␈ 66
Exercise 2-43: Find an Index of an Item in a List with the Customized Exception␈ 68
Practicing Lists␈ 69
Exercise 2-44: Practice a List␈ 69
Using for Loops and while Loops␈ 71
Exercise 2-45: Use the for Loop’s upper( ) and capitalize( ) Methods␈ 71
Exercise 2-46: Use the while Loop and len( ) Function␈ 71
Sorting and Ranges␈ 72
Exercise 2-47: Use sort( ) vs. sorted( ) in a List␈ 72
Exercise 2-48: Link Two Lists␈ 72
Exercise 2-49: Find the List Length Using the len( ) Function␈ 73
Exercise 2-50: Use range( ) and the for Loop␈ 73
Exercise 2-51: Use the String List for loop( ) and range( ) with Arguments␈ 74
Recap: Lists and Loops␈ 75
Tuples␈ 76
Exercise 2-52: See Some Basic Tuple Examples␈ 76
Exercise 2-53: Convert a Tuple to a List␈ 76
Exercise 2-54: Determine Whether a Tuple Immutable␈ 77
Exercise 2-55: Convert a Tuple to a List and a List to a Tuple␈ 78
Exercise 2-56: Use a for Loop in a Tuple␈ 78
Exercise 2-57: Assign Multiple Variables to a Tuple␈ 79
Exercise 2-58: Create a Simple Tuple Function␈ 79
Exercise 2-59: Use Tuples as List Elements␈ 80
Recap: Tuples␈ 80
Dictionaries␈ 81
Exercise 2-60: Understand Dictionary Basics␈ 81
Exercise 2-61: Avoid a Dictionary TypeError and Convert Two Lists to a Single Dictionary␈ 82
Exercise 2-62: Use Keys to Print Values from a Dictionary␈ 82
Exercise 2-63: Change a Dictionary Value␈ 83
viii■ Table of Contents
Exercise 2-64: Add a New Set of Keys and Values to a Dictionary␈ 83
Exercise 2-65: Find the Number of Dictionary Elements␈ 84
Exercise 2-66: Delete Dictionary Keys and Values␈ 84
Exercise 2-67: Write a Python Script with a Dictionary␈ 84
Exercise 2-68: Use a Dictionary for a Loop and Formatting␈ 85
Recap: Dictionaries␈ 86
Handling Files␈ 87
Exercise 2-69: Read and Display Hosts File from Your PC␈ 87
Exercise 2-70: Open and Close Hosts Files␈ 88
Exercise 2-71: Create Code to Close a File in Two Ways␈ 89
Exercise 2-72: Create a Text File, and Read, Write, and Print␈ 90
Exercise 2-73: Use rstrip( ) or lstrip( ) to Remove Whitespace␈ 93
Exercise 2-74: Python File Mode Exercise: Use r Mode␈ 94
Exercise 2-75: Python File Mode Exercise: Use r+ Mode␈ 95
Exercise 2-76: Python File Mode Exercise: Use a Mode␈ 96
Exercise 2-77: Python File Mode Exercise: Use a+ Mode␈ 99
Exercise 2-78: Python File Mode Exercise: Use w Mode␈ 99
Exercise 2-79: Python File Mode Exercise: Use w+ Mode␈ 100
Exercise 2-80: Python File Mode Exercise: Use x Mode␈ 101
Exercise 2-81: Python File Mode Exercise: Use x Mode␈ 102
Exercise 2-82: Open a Byte File in Python␈ 103
Exercise 2-83: Handle Errors with try and except␈ 104
Recap: Python file Handling Concept␈ 105
Using Python Modules␈ 105
Time Module␈ 106
Exercise 2-84: Import the time Module␈ 106
Sleep Method␈ 106
Exercise 2-85: Use the time.sleep( ) Function␈ 106
Exercise 2-86: Browse a Path Using the sys Module␈ 107
Exercise 2-87: Add a New Filepath Using the sys Module␈ 108
Exercise 2-88: Check Built-ins and sys.builtin_module␈ 109
ix■ Table of Contents
Exercise 2-89: Use a Simple import sys Module in a try and except Exercise␈ 110
Exercise 2-90: Understand Lambdas by Making a Calculator␈ 111
Recap: Module Concepts␈ 112
Summary␈ 112
■Chapter
■
3: More Python Exercises␈ 113
Getting Ready for the Exercises␈ 113
Exercise 3-1: Concatenate a List and a Tuple into a Single List␈ 114
Exercise 3-2: Use Python as a Calculator␈ 114
Exercise 3-3: Do Some Basic String format( ) Exercises␈ 114
Exercise 3-4: Ask for a Username␈ 115
Exercise 3-5: Get a Username: Version 1␈ 116
Exercise 3-6: Get a Username: Version 2␈ 117
Exercise 3-7: Get a Username: Version 3␈ 118
Exercise 3-8: Add a Temporary Filepath, Import ex3_7.py as a Module, and Run the Script␈ 120
Exercise 3-9: Use Commas to Add Spaces Between Strings␈ 120
Exercise 3-10: Practice if; if and else; and if, elif, and else␈ 121
Exercise 3-11: Practice for ~ in range with end=‘ ’␈ 122
Exercise 3-12: Practice for ~ in range␈ 123
Exercise 3-13: Practice for line in ~␈ 123
Exercise 3-14: Use the split( ) Method␈ 124
Exercise 3-15: Practice with lstrip( ), rstrip( ), strip( ), upper( ), lower( ), title( ), and capitalize( )␈ 124
Exercise 3-16: Create a file and read it four different ways␈ 125
Exercise 3-17: Read and Output Files for a More Detailed Understanding␈ 126
Exercise 3-18: Use the getpass( ) Module and User Input␈ 127
Exercise 3-19: Understand the Difference Between Encoding and Decoding␈ 128
Exercise 3-20: Handle CSV Files in Python with the csv Module␈ 128
Exercise 3-21: Output a CSV File␈ 132
Exercise 3-22: Find the Price of a Cisco ISR 4331 Router from a CSV File␈ 132
Exercise 3-23: Calculate the Total Cost of the Router Purchases: No Module␈ 133
Exercise 3-24: Calculate the Total Cost of the Router Purchases: Using the csv Module␈ 134
Exercise 3-25: Convert dd-mmm-yy and Calculate the Difference in Days and Then in Years␈ 134
x■ Table of Contents
Exploring the Python IDE Environment␈ 136
Summary␈ 137
Storytime 2: Machine vs. Human, The First Confrontation␈ 138
■Chapter
■
4: Introduction to VMware Workstation␈ 139
VMware Workstation at a Glance␈ 139
Type-1 vs. Type-2 Hypervisors␈ 141
VMware Workstation Pro for a Proof-of-Concept Lab␈ 142
Before Using VMware Workstation␈ 142
What’s Next on VMware Workstation 15 Pro?␈ 145
VMware Workstation 15 Pro User Console␈ 145
Basic Operations of VMware Workstation 15 Pro␈ 146
VMware Workstation Pro: Basic Operations␈ 147
VMware Workstation Menu␈ 149
Virtual Network Adapters␈ 152
Virtual Network Editor Overview␈ 152
Virtual Network Interface Description␈ 155
Revealing Each Virtual Network Interface Types␈ 159
Summary␈ 168
■Chapter
■
5: Creating an Ubuntu Server Virtual Machine␈ 169
Downloading and Installing a Ubuntu Server 20 Image␈ 170
Downloading the Ubuntu Server 20.04 LTS Image␈ 171
Installing Ubuntu Server 20.04 LTS␈ 172
Logging In to a New Ubuntu Server 20 via SSH␈ 196
Customize Ubuntu Server␈ 202
Ubuntu VM Customization 1: Enable Root User SSH Login on Ubuntu Server 20.04␈ 203
Ubuntu VM Customization 2: Install a Desktop GUI and Other Packages␈ 205
Ubuntu VM Customization 3: Enable Root User GUI Access␈ 210
Taking a Snapshot of a Virtual Machine␈ 214
Cloning a Virtual Machine␈ 217
Summary␈ 222
xi■ Table of Contents
■Chapter
■
6: Creating a CentOS 8 Server Virtual Machine␈ 223
Downloading and Installing a CentOS 8 Server Image␈ 223
Downloading the CentOS 8 Server Image␈ 224
Installing CentOS 8 Server␈ 226
Logging In to a New CentOS 8 Server via SSH␈ 260
Managing a Network Adapter on Linux␈ 263
Creating a GNS3 VM by Importing an .ova File␈ 269
Downloading and Installing the GNS3 VM from an .ova File␈ 270
Summary␈ 274
Storytime 3: The Origin of Hypervisors␈ 274
■Chapter
■
7: Linux Fundamentals␈ 275
Why Learn Linux?␈ 276
The Beginning of Linux␈ 278
Understanding the Linux Environment␈ 279
Understanding Linux Directories and File Formats␈ 280
vi vs. nano␈ 281
Introduction to vi␈ 282
Introduction to nano␈ 293
Linux Basic Administration␈ 306
Changing the Hostname␈ 306
Linux Basic File and Directory Commands␈ 309
Linux File and Directory Exercises␈ 311
Summary␈ 327
■Chapter
■
8: Linux Basic Administration␈ 329
Information on Linux: Kernel and Distribution Version␈ 329
Information on Linux: Use the netstat Command to Validate TCP/UDP Ports␈ 332
Installing TFTP, FTP, SFTP, and NTP Servers␈ 339
FTP Server Installation␈ 340
Installing the SFTP Server␈ 346
xii■ Table of Contents
Installing the TFTP Server␈ 350
Installing the NTP Server␈ 355
Linux TCP/IP Troubleshooting Exercise␈ 359
Summary␈ 364
Storytime 4: Becoming a Savvy Linux Administrator, Perhaps Every IT
Engineer’s Dream?␈ 364
■Chapter
■
9: Regular Expressions for Network Automation␈ 367
Why Regex?␈ 368
To re or Not to re␈ 369
Studying Regular Expressions Using Python␈ 371
Method 1: Using Notepad++␈ 372
Method 2: Using the Linux Shell␈ 374
Regular Expression Breakdown: [A-Z]{3}\d{4}[/]\w+␈ 375
Method 3: Using the Internet to Study Regular Expressions␈ 375
Regex Operation: The Basics␈ 376
Character Class ([])␈ 378
Dot (.): Single Character Match␈ 379
Asterisk (*): Repetition␈ 380
Plus (+): Repetition␈ 380
{m, n}: Repetition␈ 380
Python’s re Module␈ 382
Python re String Methods␈ 383
Match Object Method␈ 387
Compile Options␈ 388
re.DOTALL (re.S)␈ 389
re.IGNORECASE (re.I)␈ 389
re.MULTILINE (re.M)␈ 390
re.VERBOSE (re.X)␈ 391
\: Confusing Backslash Character␈ 392
Regular Expressions: A Little Revision Plus More␈ 393
More Metacharacters␈ 393
xiii■ Table of Contents
Lookahead and Lookbehind Assertions␈ 403
Lookahead, Lookbehind, and Noncapturing group␈ 403
Practice More Lookarounds␈ 405
Lookaround Application Examples␈ 407
sub Method: Substituting Strings␈ 409
Substitute Strings Using sub␈ 410
Using sub and \g to Swap Positions␈ 410
Insert a Function in sub Method␈ 411
Summary␈ 413
■Chapter
■
10: GNS3 Basics␈ 415
GNS3 at a Glance␈ 415
Installing GNS3 for the First Time␈ 417
Downloading the GNS3 Installation File␈ 417
GNS3 Installation and Setup␈ 418
GNS3 Installation␈ 418
GNS3 Setup Procedures␈ 418
Getting Familiar with GNS3␈ 424
GNS3 Menus and GUI␈ 424
Gracefully Shutting Down GNS3 and GNS3 VM␈ 426
Starting GNS3 as an Administrator␈ 428
Using GNS3 for the First Time: Cisco IOS and Windows Lab␈ 429
Cisco IOS Software License and Downloading an Older Cisco IOS␈ 430
Decompressing Cisco IOS for GNS3 Use␈ 431
Installing Cisco IOS on the GNS3 VM␈ 442
Creating an IOS Lab Topology on GNS3 and Connecting to the Internet␈ 454
Installing the Microsoft Loopback Adapter␈ 462
Accessing GNS3 Network Devices Using MS Loopback␈ 469
Configuring the GNS3 IOS Router Using a Python Script from the Windows
Host PC␈ 478
xiv■ Table of Contents
Cisco IOS and GNS3 Appliance Lab␈ 482
Importing and Installing the GNS3 Linux Appliance Server␈ 482
Manually Assigning IP Address to GNS3 Linux Appliance Server␈ 486
Using the GNS3 Appliance Linux’s Python to Manage R1␈ 487
Summary␈ 489
■Chapter
■
11: Cisco IOS Labs␈ 491
Cisco IOS and the Linux VM Lab␈ 491
Creating a New GNS3 Project for the Linux VM Lab␈ 492
Uploading and Downloading Files to the GNS3 IOS Router from Linux VMs
(File Transfer Testing Lab)␈ 503
Copying (Cloning) a GNS3 Project␈ 511
Summary␈ 514
■Chapter
■
12: Building a Python Automation Lab Environment␈ 515
Cisco CML-PERSONAL Software License Information and Software Downloads␈ 516
Downloading the Cisco CML-PERSONAL IOSvL2 (Switch) Image␈ 516
Downloading the Cisco CML-PERSONAL IOSv (Router) Image and
startup_config Files␈ 517
Installing the Cisco CML-PERSONAL L2 Switch and CML-PERSONAL L3 on GNS3␈ 518
Installing the Cisco CML-PERSONAL L2 Switch on GNS3␈ 518
Quick Communication Test on CML L2 Switch Integration on GNS3␈ 528
Installing the Cisco CML-PERSONAL L3 Router on GNS3␈ 529
Quick Communication Test on CML L3 Router Integration on GNS3␈ 539
Building a CML-PERSONAL Lab Topology␈ 541
Summary␈ 548
■Chapter
■
13: Python Network Automation Lab: Basic Telnet␈ 549
Python Network Automation: Telnet Labs␈ 549
Telnet Lab 1: Interactive Telnet Session to Cisco Devices on a Python Interpreter␈ 551
Telnet Lab 2: Configure a Single Switch with a Python Telnet Template␈ 557
Telnet Lab 3: Configure Random VLANs Using a for Loop␈ 562
xv■ Table of Contents
Telnet Lab 4: Configure Random VLANs Using a while Loop␈ 566
Telnet Lab 5: Configure 100 VLANs Using the for ~ in range Loop Method␈ 569
Telnet Lab 6: Add a Privilege 3 User on Multiple Devices Using IP Addresses
from an External File␈ 573
Telnet Lab 7: Taking Backups of running-config (or startup-config) to
Local Server Storage␈ 579
Summary␈ 582
■Chapter
■
14: Python Network Automation Labs: SSH paramiko and netmiko␈ 583
Python Network Automation Labs Using the paramiko and netmiko Libraries␈ 583
Python SSH Labs: paramiko␈ 584
paramiko Lab 1: Configure the Clock and Time Zone of All Devices Interactively
in the Python Interpreter␈ 584
paramiko Lab 2: Configuring an NTP Server on Cisco Devices Without
User Interaction (NTP Lab)␈ 592
paramiko Lab 3: Create an Interactive paramiko SSH Script to Save Running
Configurations to the TFTP Server␈ 598
Python SSH Labs: netmiko␈ 605
netmiko Lab 1: netmiko Uses a Dictionary for Device Information,
Not a JSON Object␈ 606
netmiko Lab 2: Develop a Simple Port Scanner Using a Socket Module and Then
Develop a nemiko Disable Telnet Script␈ 614
netmiko Lab 3: config compare␈ 621
Summary␈ 628
■Chapter
■
15: Python Network Automation Labs: cron and SNMPv3␈ 629
Cron and SNMPv3 Labs␈ 629
Cloning a GNS3 Project for the Next Lab␈ 630
Quick-Start to the Linux Scheduler, cron␈ 637
Ubuntu 20.04 LTS Task Scheduler: crontab␈ 637
CentOS8.1 Task Scheduler: crond␈ 641
Learn cron Job Definitions with Examples␈ 646
xvi■ Table of Contents
Using Python to Run an SNMPv3 Query␈ 648
Quick-Start Guide to SNMP␈ 649
Learn to Use SNMPwalk on a Linux Server␈ 653
Borrowing Some Example Python SNMP Code␈ 666
Summary␈ 673
■Chapter
■
16: Python Network Automation Labs: Ansible, pyATS, Docker,
and the Twilio API␈ 675
Python Network Automation Development Labs␈ 675
Quick-Start Guide to Ansible: virtualenv Lab 1␈ 676
Installing virtualenv and Getting Started with Ansible␈ 678
Quick-Start Guide to pyATS (Genie): VirtualEnv Lab 2␈ 685
Sendmail Lab Using an Imported Docker Image␈ 700
Docker Components and Account Registration␈ 701
Docker Installation␈ 702
Test-Driving Docker␈ 703
Docker Sendmail Python Lab␈ 707
Lab: Sendmail Email Notification script Development␈ 712
CPU Utilization Monitoring Lab: Send an SMS Message Using Twilio␈ 717
TWILIO Account Creation, Install Twilio Python Module and SMS Message Setup␈ 718
CPU Utilization Monitoring Lab with an SMS Message␈ 723
Summary␈ 732
■Chapter
■
17: Upgrading Multiple Cisco IOS XE Routers␈ 733
Practical Python Network Automation Lab: IOS XE Upgrade Lab␈ 733
Applying OOP Concepts to Your Network␈ 734
Flow Control and Controlling User Input: UID, PWD, and Information Collector␈ 738
Lab Preparation␈ 743
CSR 1000v IOS XE Software and Download␈ 744
Cisco CSR 1000v Installation on VMware Workstation␈ 745
xvii■ Table of Contents
Discussion of How an IOS (IOS-XE/XR) Is Upgraded on Cisco Devices␈ 756
Tasks Involved in a Cisco IOS Upgrade␈ 756
Summary␈ 759
■Chapter
■
18: Python Network Automation Lab: Cisco IOS Upgrade
Mini Tools Development␈ 761
Cisco IOS Upgrade Application Development␈ 761
Part A: Pre-check Tools Development Connectivity Validation Tool␈ 762
Collect User’s Login Credentials and User Input␈ 774
Collect a New IOS Filename and MD5 Value from a CSV File␈ 778
Check the MD5 Value of the New IOS on the Server␈ 788
Check the Flash Size on Cisco Routers␈ 792
Make Backups of running-config, the Interface Status, and the Routing Table␈ 796
Part B: IOS Uploading and More Pre-check Tools Development␈ 799
IOS Uploading Tool␈ 799
Check the New IOS MD5 Value on the Cisco Device’s Flash␈ 804
Options to Stop or Reload the Routers␈ 810
Check the Reloading Device and Perform a Post-Reload Configuration Verification␈ 819
Summary␈ 829
■Chapter
■
19: Python Network Automation Labs: Combining and
Completing the Cisco IOS Upgrade Application␈ 831
Creating a Single Python File␈ 832
Summary␈ 852
Final Words␈ 853
Index␈ 855
