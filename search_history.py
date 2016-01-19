#!/usr/bin/env python

import getpass
import json
import os

from ricloud.api import RiCloud
from credentials import APPLE_ID, APPLE_PASSWORD

api = RiCloud()
api.login(APPLE_ID, APPLE_PASSWORD)

for device in api.devices:
    data = api.backup_client.request_data(device_id=device, data_mask=4)
    print device, data
