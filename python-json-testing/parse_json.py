import json
from pprint import pprint

with open('channel_obj.json') as data_file:
    data = json.load(data_file)

pprint(len(data['messages']))
