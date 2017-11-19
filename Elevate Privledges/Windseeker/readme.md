Android package file
The Trojan may arrive as a package with the following characteristics:

Package name: com.example.windseeker
Version: 2.1
Name: Wind Seeker

Permissions
When the Trojan is being installed, it requests permissions to perform the following actions:

    Open network connections
    Write to external storage devices
    Get information about currently or recently running tasks
    Read or write to the system settings
    Start once the device has finished booting
    Check the phone's current state
    Send SMS messages
    Access information about networks

Installation
Once installed, the application will display an icon with a green Android icon with a box on its chest.

Functionality
When the Trojan is executed, it requests a root permission and creates the following service to run in the background:
    com.example.chathook.ProcessMonitor

When the Trojan obtains root permissions, it creates the following files to monitor activities in the QQ and Wechat messengers:

    *competing_su
    *libcall.so
    *inject_appso
    *conn.jar

The Trojan steals the following information:

    Contact information
    Chat history of messengers

Resource 
http://blog.csdn.net/mobisec/article/details/39103593
http://contagiominidump.blogspot.com/2014/10/android-chathook-ptrace.html
https://www.scmagazine.com/windseeker-app-spies-on-chats-using-injection-hooking-techniques/article/539862/
https://www.mysonicwall.com/sonicalert/searchresults.aspx?ev=article&id=734