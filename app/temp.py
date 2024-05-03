import json
from pprint import pprint
with open('candidates_data3.json') as f:
    d = json.load(f)
    pprint(d[0])