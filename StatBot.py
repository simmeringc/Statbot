import time
import os
import json
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint
from urllib import urlopen
from slackbot import settings
from collections import defaultdict
from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re

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

    @respond_to('channel_analytics', re.IGNORECASE)
    def channel_analytics(message):

        N = 5
        menMeans = (20, 35, 30, 35, 27)
        menStd = (2, 3, 4, 1, 2)

        ind = np.arange(N)  # the x locations for the groups
        width = 0.35       # the width of the bars

        fig, ax = plt.subplots()
        rects1 = ax.bar(ind, menMeans, width, color='r', yerr=menStd)

        womenMeans = (25, 32, 34, 20, 25)
        womenStd = (3, 5, 2, 3, 3)
        rects2 = ax.bar(ind + width, womenMeans, width, color='y', yerr=womenStd)

        # add some text for labels, title and axes ticks
        ax.set_ylabel('Scores')
        ax.set_title('Scores by group and gender')
        ax.set_xticks(ind + width)
        ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5'))

        ax.legend((rects1[0], rects2[0]), ('Men', 'Women'))


        def autolabel(rects):
            # attach some text labels
            for rect in rects:
                height = rect.get_height()
                ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                        '%d' % int(height),
                        ha='center', va='bottom')

        autolabel(rects1)
        autolabel(rects2)

        plt.show()
        message.reply('graphing')
