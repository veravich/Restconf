#!/usr/bin/env python
"""
Sample Restconf POST Request for vpn endpoints.
Need: pip3 install requests
Usage: python3 restconf4.py
Note: Toggle USE_HTTPS in line 26 for HTTPS or HTTP access
"""


import json
import requests
from collections import OrderedDict
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

url = url_base + "/data/l3vpn:vpn/l3vpn=abc-bank"

# Build the data payload to create a new vpn site
# Need to use OrderedDicts to maintain the order of elements

data = OrderedDict([('l3vpn:endpoint',
              OrderedDict([
                        ('id', 'branch9'),
                        ('ce-device', 'ce6'),
                        ('ce-interface', 'GigabitEthernet0/3'),
                        ('ip-network', '10.6.0.0/24'),
                        ('bandwidth', 1500),
                        ('as-number', 65006)
                        ])
                        )])

# Use POST request to create new vpn site
response = requests.post(url,
                        auth=(USER, PASS),
                        headers=headers,
                        verify=False,
                        json=data
                        )

#printing request and response
print ('\n\nAPI: ', url)
print ('\nPayload: \n')
print (json.dumps(data,indent=4))
print ('\nResponse Code: ', response.status_code, '\n\n')
