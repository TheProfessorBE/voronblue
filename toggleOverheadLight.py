import requests
import json
import os

#FILENAME = '/home/pi/klipper_config/lightToggleFile.dat'

FILENAME = "storage"
url = 'http://energysocket-2933CE.local/api/v1/state'
headers = {"Content-Type": "application/json"}

response = requests.get(url )
response_json = response.json()
json_data = json.loads(response.text)

if(json_data['power_on']):
    input_dict = {'power_on': False, 'switch_lock': False, 'brightness': 1}
else:
    input_dict = {'power_on': True, 'switch_lock': False, 'brightness': 1}

response = requests.put(url, data=json.dumps(input_dict), headers=headers)