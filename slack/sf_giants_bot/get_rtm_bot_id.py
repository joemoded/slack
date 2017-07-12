import os, slackclient


# to run, "python get_rtm_bot.py
# after running, export BOT_ID to virtualenv using command line
# before running, export BOT_NAME and BOT_TOKEN to virtualenv using command line
BOT_NAME = os.environ.get('BOT_NAME')
BOT_TOKEN = os.environ.get('BOT_TOKEN')

# initialize slack client and print BOT_ID in command line
slack_client = slackclient.SlackClient(BOT_TOKEN)
print slack_client
client_connect = slack_client.api_call("users.list").get('ok')
print client_connect
for user in slack_client.api_call("users.list").get('members'):
    if user.get('name') == BOT_NAME:
        print user.get('id')
