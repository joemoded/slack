import os, slackclient, time
from players import players


BOT_NAME = os.environ.get('BOT_NAME')
BOT_TOKEN = os.environ.get('BOT_TOKEN')
BOT_ID = os.environ.get('BOT_ID')


# initialize slack client
slack_client = slackclient.SlackClient(BOT_TOKEN)


# how the bot is mentioned on slack
def get_bot_mention(user):
    return '<@{user}>'.format(user=user)

bot_mention = get_bot_mention(BOT_ID)


# look for player mentioned by user in players file
def player_finder(message):
    headshot = 'http://mlb.mlb.com/mlb/images/players/head_shot/'

    if 'list players' in message:
        return 'list'

    player = True
    for key, value in players.iteritems():
        message = message.lower()
        if key in message:
             player = value
    if player != True:
        return headshot + player + '.jpg'
    else:
        return True


def handle_message(message, channel):
    if player_finder(message):
        post_message(message=player_finder(message), channel=channel)


# post image of player, list players, or ask user to further specify player name
def post_message(message, channel):
    print message
    if message is True:
        attachments = [
            {
            "fallback": "player not found",
            "text": 'We could not find that player.  Try using their first and last name. To view a list of all current '
                    'players on the Giants 40 man roster, type "list players"',
            "image_url": 'https://media.giphy.com/media/rNREgYn3gwFkA/giphy.gif'
            }
                ]
    elif message is 'list':
        giants_players = sorted(list(players.keys()))
        attachments = [
            {
            "fallback": "player list",
            "text": 'Current Giants 40 man roster:\n' + str("\n ".join(giants_players).title())
            }
        ]
    else:
        attachments = [
            {
                "fallback": "player found",
                "image_url": message
            }

        ]
    icon_url = 'http://png-2.vector.me/files/images/7/4/74446/san_francisco_giants_thumb.png'
    slack_client.api_call('chat.postMessage',
                          channel=channel, attachments=attachments,
                          icon_url=icon_url, as_user=True)


def message_to_bot(event):
    type = event.get('type')
    #if event is a message and is not from the bot
    if type and type == 'message' and not(event.get('user')==BOT_ID):
        text = event.get('text')
        #check if message is for bot
        if bot_mention in text:
            return True


def run():
    socket_delay = 1
    #check if slack is connected to RTM API
    if slack_client.rtm_connect():
        print('[.] Connected to RTM API...')
        while True:
            #check for events every 1 second
            event_list = slack_client.rtm_read()
            if len(event_list) > 0:
                for event in event_list:
                    #grab text messages sent to bot
                    if message_to_bot(event):
                        handle_message(message=event.get('text'), channel=event.get('channel'))
            time.sleep(socket_delay)
    else:
        print('[!] Connection to Slack failed.')

if __name__=='__main__':
    run()







