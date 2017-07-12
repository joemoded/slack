
**Using RTM and events API**
With this exercise, I have included two bot integrations, one which uses the RTM api (sf_giants_bot), and another
which uses the events api (channel_events_bot).


**What do these bots do?**
sf_giants_bot uses RTM api to do the following:
    - Display headshots of current San Francisco Giants
    - If player isn't found, instructs user to type 'list players' in order to view all available players
    - 'List players' displays all current San Francisco Giants 40-man roster

channel_events_bot uses events api to do the following:
    - Notifies general channel when separate channel is created, deleted, or renamed


**Setup:**
To run, you will first need to set up a virtual environment. If you don't yet have virtualenv installed, run the
following in command line:

Install virtualenv::

    pip install virtualenv

Set up virtual environment::

    virtualenv env

Activate virtual environment::

    source env/bin/activate

Install slackclient::

    pip install slackclient

Install slackeventsapi::

    pip install slackeventsapi


**Run SF Giants Bot**
In order to run this locally, I have included the bot tokens in the tokens.ini file for each bot.

In command line virtualenv, run the following::

    export BOT_TOKEN='xoxb-210743843584-bLvGNkpMtMeOdePDk3G7n7Nh'
    export BOT_NAME='sf-giants'
    export BOT_ID='U66MVQTH6'

Start bot::

    python sf_giants_bot.py

Once the bot is running, feel free to interact with it in the slack channels.  Example inputs would be the following:
    @sf_giants buster posey
    @sf_giants madison bumgarner
    @sf_giants hunter pence
    @sf_giants list players

The bot will also take incorrect inputs and let the user know that they didn't recognize the input


**Run Channel Events bot**
If you don't already have your virtualenv set up, go back to setup instructions.  Once your virtualenv is running,
export the tokens in command line to run the bot locally::

    export CLIENT_VERIFICATION_TOKEN='FmJX27voE84OhCpp5jKCZk48'
    export SLACK_BOT_TOKEN='xoxb-211407425618-VufyooaOosqIhwCokf5a04jo'

Start bot::

    python channel_events_bot.py

Connect to local server:
    For this exercise I used ngrok to set up and contact a local server.  Available at "https://ngrok.com/"

Once ngrok has been installed, run::

    ngrok http 3000

- Copy the forwarding https address given by ngrok
- Navigate to https://api.slack.com/apps/A66MRBS3A/event-subscriptions
- Paste https address + '/slack/events' in request url and save


Once the bot is running, create, rename, or delete a channel and view response in general channel.














