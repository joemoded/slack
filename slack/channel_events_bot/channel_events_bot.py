from slackeventsapi import SlackEventAdapter
import slackclient
import os


CLIENT_VERIFICATION_TOKEN = os.environ["CLIENT_VERIFICATION_TOKEN"]
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]

slack_events_adapter = SlackEventAdapter(CLIENT_VERIFICATION_TOKEN, "/slack/events")
slack_client = slackclient.SlackClient(SLACK_BOT_TOKEN)


# post to general when new channel is created
@slack_events_adapter.on('channel_created')
def channel_created(event_data):
    event = event_data['event']
    channel = event['channel']
    channel_name = channel.get('name')
    text = 'A new channel has been created: "' + channel_name + '"'
    general = '#general'
    slack_client.api_call('chat.postMessage', channel=general, text=text)


# post to general when channel is deleted
@slack_events_adapter.on('channel_deleted')
def channel_deleted(event_data):
    event = event_data['event']
    text = 'A channel has been deleted.'
    general = '#general'
    slack_client.api_call('chat.postMessage', channel=general, text=text)


# post to general when channel is renamed
@slack_events_adapter.on('channel_rename')
def channel_renamed(event_data):
    event = event_data['event']
    channel = event['channel']
    channel_name = channel.get('name')
    text = 'A channel has been renamed: "' + channel_name + '"'
    general = '#general'
    slack_client.api_call('chat.postMessage', channel=general, text=text)


# Start Flask server with default port 3000
slack_events_adapter.start(port=3000)
