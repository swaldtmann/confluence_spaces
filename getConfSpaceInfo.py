# -*- coding: UTF-8 -*-
# getConfSpaceInfo.py


import requests
import json
import os 
import pandas

from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

from pprint import pprint


# Load environment variables from `.env` file.
#
# Have a .env file in the directory of this script, containing:
"""
# .env 
ATLASSIAN_USERNAME=<your username here>
ATLASSIAN_PASSWORD=<your password here>

# your url may look like: https://wiki.example.com/rest/api/space?limit=500
ATLASSIAN_URL=<your url here>

#
# End of .env
"""

load_dotenv()
# Your values are now stored in `os.environ`

### Variables
username = os.environ.get('ATLASSIAN_USERNAME', '')
password = os.environ.get('ATLASSIAN_PASSWORD', '')
url = os.environ.get('ATLASSIAN_URL', '')

spaces = list()
outfilename = "conf-keys_20220319.csv"

### Main
auth = HTTPBasicAuth(username, password)
headers = {"Content-type": "application/json"}
response = requests.request("GET", url, headers=headers, auth=auth)

# If the HTTP GET request can be served
if response.status_code == 200:
    print(response.text)
    data = json.loads(response.text)


    df = pandas.DataFrame(data["results"])

    df.pop('_links')
    df.pop('_expandable')

    #df = pandas.read_json(response.text)
    df.to_csv(outfilename, encoding='utf-8-sig')
    print(df)
else:
    print("Could not load Page! Exiting ...")
    