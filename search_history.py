#!/usr/bin/env python

import getpass
import json
import os

from ricloud.api import RiCloud

# example of credentials file
example_credentials = "APPLE_ID='foo@bar.com'\nAPPLE_PASSWORD=1234"

# check for the credentials file
if os.path.isfile('./credentials.py'):
    from credentials import APPLE_ID, APPLE_PASSWORD
else:
    print "credentials.py file missing, please create one. ie:\n{cred}".format(cred=example_credentials)
    raise SystemExit

# if all exists, try and connect to the api
api = RiCloud()
api.login(APPLE_ID, APPLE_PASSWORD)

# then request history for each device
for device in api.devices:
    data = api.backup_client.request_data(device_id=device, data_mask=4)
    print device, data
