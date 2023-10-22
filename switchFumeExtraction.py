import argparse
import string
import requests
import json
import os

FILENAME = "storage"
url = 'http://energysocket-0d5d7e.local/api/v1/state'
headers = {"Content-Type": "application/json"}



argParser = argparse.ArgumentParser()
argParser.add_argument("-s", "--state", type=str, help="State")
argParser.add_argument("-p", "--power", type=float, help="Power Percentage")


argsOut = argParser.parse_args()
print("args=%s" % argsOut)


if(argsOut.state == 'ON' or argsOut.state == 'On' or argsOut.state == 'on'):
    print("On")
    input_dict = {'power_on': True, 'switch_lock': False, 'brightness': 1}
    

elif(argsOut.state == 'OFF' or argsOut.state == 'Off' or argsOut.state == 'off'):
    print("off")
    input_dict = {'power_on': False, 'switch_lock': False, 'brightness': 1}

else:
    print( "Unknown Command")

response = requests.put(url, data=json.dumps(input_dict), headers=headers)