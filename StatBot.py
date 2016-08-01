import time
import os
import re
import json
import plotly.plotly as py
import plotly.graph_objs as go
import subprocess
from pprint import pprint
from urllib import urlopen
from slackbot import settings
from collections import defaultdict
from slackbot.bot import respond_to
from slackbot.bot import listen_to

@respond_to('help', re.IGNORECASE)
def help(message):
    help_reply = {
    "text": "You can ask me one of the following questions:\n * channel_stats \n * channel_analytics"
    }
    message.reply(help_reply['text'])

@respond_to('channel_stats', re.IGNORECASE)
def channel_stats(message):

    # Slack user web API token
    token = os.environ.get('USER_TOKEN')

    # Total message count
    channel_endpoint = urlopen('https://slack.com/api/channels.history?token='+token+'&channel=C1R5Z1FT3&count=1000&pretty=1').read()
    channel_endpoint_result = json.loads(channel_endpoint)
    total_message_count = str(len(channel_endpoint_result['messages']))

    # Individual message count
    users_endpoint=urlopen('https://slack.com/api/users.list?token='+token+'&pretty=1').read()
    users_endpoint_result = json.loads(users_endpoint)
    users_arr = []
    for i in users_endpoint_result['members']:
        data = []
        data.append(i['name'])
        data.append(i['id'])
        users_arr.append(data)
    pprint(users_arr)
    count_dict = defaultdict(int)
    len_user_arr = len(users_arr)
    for i in range(0, len_user_arr):
        count_dict[users_arr[i][1]] = 0
    pprint(count_dict)
    for i in channel_endpoint_result['messages']:
        for j in range(0,len_user_arr):
            if i['user'] == users_arr[j][1]:
                count_dict[users_arr[j][1]] += 1
    pprint(count_dict)
    key_arr = []
    for key in count_dict:
        key_arr.append(key)
    pprint(key_arr)
    for i in range(0,len_user_arr):
        for j in range(0, len_user_arr):
            if key_arr[i] == users_arr[j][1]:
                count_dict[users_arr[j][0]] = count_dict.pop(key_arr[i])
    str_count_dict = str(count_dict)

    # Answer command
    channel_stats_reply = {
    "text": "Channel Stats:\n Total channel messages: "+total_message_count+"\n"+str_count_dict+""
    }
    message.reply(channel_stats_reply['text'])

# Hardcoded graph but with real data
@respond_to('channel_analytics', re.IGNORECASE)
def channel_analytics(message):

    # Slack user web API token
    token = os.environ.get('USER_TOKEN')

    users_endpoint=urlopen('https://slack.com/api/users.list?token='+token+'&pretty=1').read()
    users_endpoint_result = json.loads(users_endpoint)
    users_arr = []
    for i in users_endpoint_result['members']:
        data = []
        data.append(i['name'])
        data.append(i['id'])
        users_arr.append(data)

    count_dict = defaultdict(int)
    len_user_arr = len(users_arr)
    channel_endpoint = urlopen('https://slack.com/api/channels.history?token='+token+'&channel=C1R5Z1FT3&count=1000&pretty=1').read()
    channel_endpoint_result = json.loads(channel_endpoint)
    for i in channel_endpoint_result['messages']:
        for j in range(0,len_user_arr):
            if i['user'] == users_arr[j][1]:
                count_dict[users_arr[j][1]] += 1

    pprint(count_dict)
    pprint(count_dict[users_arr[0][1]])

    labels=[users_arr[0][0],users_arr[1][0],users_arr[2][0],users_arr[3][0],users_arr[4][0],users_arr[5][0],users_arr[6][0],users_arr[7][0]]

    values=[count_dict[users_arr[0][1]],count_dict[users_arr[1][1]],count_dict[users_arr[2][1]],count_dict[users_arr[3][1]],count_dict[users_arr[4][1]],count_dict[users_arr[5][1]],count_dict[users_arr[6][1]], count_dict[users_arr[7][1]]]

    trace=go.Pie(labels=labels,values=values)
    py.iplot([trace])

    message.reply('https://plot.ly/~simmeringc/39/')
