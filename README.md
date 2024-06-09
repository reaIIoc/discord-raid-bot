# Bot status
the Order 66 bot is still in Beta, contributions will be made to it. It's not user friendly as of right now but I will work towards making this bot 
extremely userfriendly. 

# Bot Features
1. Removes all users from the discord server
2. Deletes all channels and replaces with clones-are-resting-here channel names

# How to use? 
1. So make an account over at https://discord.com/developers/

2. then after you've created a bot, you'll need to grab the login Token in Bot > TOKEN , this is important and required in order to
   run the bot as it uses that unique token to login to the discord API.

3. From there, go to your discord account settings > Advanced > Developer Mode enable developer mode.

4. You need to get the server ID of the server you want to execute the bot on, you can do this by right clicking and selecting Copy Server ID.
   Slap that bad boy into the section inside the script that says "ENTER SERVER ID MUST BE INTEGER!" Remove quotes when inputting the integer value.

5. After you've done that head over to https://discord.com/developers/applications using the account you made earlier to 
   create the bot or application rather, click on the application you made earlier (bot) then navigate to the installation tab, click install link
   set that to "Discord provided link", slap that URL into your webbrowser, and add that puppy straight into the server.

6. Open the main.py script using any sort of text editor, notepad works fine. After you've done that change the const variable USERNAME to whatever your
   discord username is. 

8. After you've done all that, ensure you have python installed, if you do not have python installed, https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe go         through the setup wizard and make sure you install python to the PATH environment variable during the setup. After you've done that simply double click the main.py file.      After you've done that all you need to type is **Execute order 66** into the server. this triggers the script.

NOTE: you need manage server permissions in order to do this yourself unless you want to utilise social engineering, excellent method of 

# Additional info
The script uses multitprocessing which starts two parent threads and joins the threads into the main thread running the python
interpreter itself so as long as your CPU has more than 3 threads you'll be apples, pretty sure everyone does.? Unless you've got a potato. 

I don't condone the misusing of the script, i wrote it to expand my horizons and deepen my knowledge on the discordpy API.

Thank you. 
