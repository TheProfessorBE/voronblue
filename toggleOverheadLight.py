import requests
import json
import os

FILENAME = '/home/pi/klipper_config/lightToggleFile.dat'

#FILENAME = "storage"
if( os.path.exists( FILENAME ) ):
    print( "on" )
    url = 'http://energysocket-2933CE.local/api/v1/state'
    input_dict = {'power_on': True, 'switch_lock': False, 'brightness': 1}
    headers = {"Content-Type": "application/json"}
    response = requests.put(url, data=json.dumps(input_dict), headers=headers)
    
    os.remove(FILENAME)
    
else:
    print("off")
    url = 'http://energysocket-2933CE.local/api/v1/state'
    input_dict = {'power_on': False, 'switch_lock': False, 'brightness': 1}
    headers = {"Content-Type": "application/json"}
    response = requests.put(url, data=json.dumps(input_dict), headers=headers)

    f = open(FILENAME, "w")
