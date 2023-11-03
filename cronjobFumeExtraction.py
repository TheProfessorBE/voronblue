import requests
import json
import sys

urlBuffer = []
urlBuffer.append('http://voronred.local/api/printer')
urlBuffer.append('http://voronblue.local/api/printer')

headers = {"Content-Type": "application/json"}

numberPrintersPrinting = 0
for urlInput in urlBuffer:
    print(urlInput)

    response = requests.get(urlInput)
    response_json = response.json()
    json_data = json.loads(response.text)
    print(json_data["state"]["text"])
    if(json_data["state"]["text"] == "Printing" ):
        numberPrintersPrinting += 1

if( numberPrintersPrinting > 0):
    input_dict = {'power_on': True, 'switch_lock': False, 'brightness': 1}
    print("There are printers printing. Switching fume fan on")
else:
    input_dict = {'power_on': False, 'switch_lock': False, 'brightness': 1}
    print("Nobody is printing. Switching fume fan off")

print(input_dict)
numberRetries = 0
successSwitch = 0
for cntRetry in range(0, 5):
    try:
        response = requests.put('http://energysocket-0d5d7e.local/api/v1/state', data=json.dumps(input_dict), headers=headers)
        successSwitch = 1
        print("Succes switching state")
        print(response)
    except:
        numberRetries += 1
        print("Doing a retry")
    if( successSwitch == 1):
        break
        print("Beaking out of the retry loop")









