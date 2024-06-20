# Bot status
the raid bot is still in it's early stages of development but I will contribrute to the source code whenever i can. 

# Bot Features
1. Removes all users from the discord server (except for the AUTH_USER)
2. Removes all channels and creates channels named "hacked-by-raidbot"

# Important information
Before you use the bot you will need to make configurations in accordance with the comments within the source code. 

**How to add username to AUTH_USER and updating other variables?**

You can do so by ensuring any of the data that is commented out to change is in the two quotation marks "", example: AUTH_USER = "exampleuser"

**How to get login token?**

Regarding login tokens, you need to login to the discord developer portal, create a bot and obtain your application token. 

**How to get server ID?**

Settings > Advanced > Enable developer settings (All within discord by the way.)

# Additional info
The script uses multitprocessing which starts two parent threads and joins the threads into the main thread running the python
interpreter itself so as long as your CPU has more than 3 threads you'll be apples, pretty sure everyone does.? Unless you've got a potato. (fret not i'm also a broke boy)

I don't condone the misusing of the script, i wrote it purely to expand my horizons and deepen my knowledge on the discordpy API.

Thank you. 
