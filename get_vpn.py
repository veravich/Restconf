#!/usr/bin/env python
"""
Sample Restconf GET Request for vpn endpoints.
Need: pip3 install requests
Usage: python3 restconf3.py
Note: Toggle USE_HTTPS in line 23 for HTTPS or HTTP access
"""

import json
import requests
import urllib3

# Disable SSL Warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Connectivity Settings
HOST = 'localhost'
HTTPS_PORT = '8888'
HTTP_PORT = '8080'
USER = 'admin'
PASS = 'admin'

USE_HTTPS = True 

# Create the base URL for RESTCONF calls
if USE_HTTPS:
    url_base = "https://{h}:{p}/restconf".format(h=HOST, p=HTTPS_PORT)
else:
    url_base = "http://{h}:{p}/restconf".format(h=HOST, p=HTTP_PORT)

# Identify yang+json as the data formats
headers = {'Content-Type': 'application/yang-data+json',
           'Accept': 'application/yang-data+json'}

# Function to retrieve the list of endpoints for the vpn
url = url_base + "/data/vpn/l3vpn=abc-bank/endpoint"

# this statement performs a GET on the specified url
response = requests.get(url,
                        auth=(USER, PASS),
                        headers=headers,
                        verify=False
                        )

# Print the result
print ('\n\nAPI: ', url)
print ('\nResponse: ')
print (response.text)

