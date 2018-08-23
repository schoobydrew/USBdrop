# USBdrop
A friendly way to do a social engineering test without actually opening a backdoor onto a client's computer

If you want to change any of the source code, you will need to recompile to get the icon back. I use pyinstaller

pip install pyinstaller

pyinstaller -F -i icon.ico script.py

USB Drop Documentation The point of this USB drop is not to compromise a machine or network, it is a test to see if a company is susceptible to social engineering attacks. Server side: Not much needs to be done here unless you want to edit how the server logs connections. Requirements: Python

Client side: A demo of the drop should be in the repository, basically you would copy over all of the files and hide everything but the fake applications. There are a bunch of files related to the executable. For some reason the antivirus wants to delete the exe when it’s one file, so just hit “hide” in the properties tab. Configuration:

Run the server, it is now listening for connections
Get a fresh USB drive and copy everything from the Drop folder into the USB as is
Go into the configuration folder
Set the IP for the server and the port that the server is configured to be listening
Set the company name or identifiable number for once the test is complete to search the logs
Back out to the home folder of the USB
Select the folder, and all of the files except for the word/ppt/excel and change their property to be hidden
Change the names of the word/ppt/excel to something juicy to entice your victims users to click on them a.	Ex: Payroll Request.docx
Drop the USB somewhere to be found
