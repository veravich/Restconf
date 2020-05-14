#! /usr/bin/env python
"""
Sample Restconf Query using HTTPS with a self-signed certificate or HTTP
"""

import requests
import urllib3

# Disable SSL Warnings
#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Device Information
HOST = 'localhost'
HTTPS_PORT = '8888'
HTTP_PORT = '8080'
USER = 'admin'
PASS = 'admin'

USE_HTTPS = True 

# Create the base URL for RESTCONF calls
if USE_HTTPS:
    url = "https://{host}:{port}/.well-known/host-meta".format(host=HOST, port=HTTPS_PORT)
else:
    url = "http://{host}:{port}/.well-known/host-meta".format(host=HOST, port=HTTP_PORT)

# Do GET Request
response = requests.get(url,
                        auth = (USER, PASS),
                        verify = False
                       )

# Print the response
print ('\n\nAPI: ', url)
print('\nResponse: \n', response.text)
