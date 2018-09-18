import json_export
import time

def generate(unit_id, owner):
    # Format: Unit ID, Date/time, type, owner, value
    timestamp = time.localtime()
    data = {
       	"unit_id": unit_id,
       	"date_time": [timestamp[0], timestamp[1], timestamp[2], timestamp[3], timestamp[4]],
       	"type": "temperature",
       	"owner": owner,
       	"value": 50 # Replace w/ random value
    }
    return data

def countdown(t):
    while t:
        time.sleep(1)
        t -= 1

while True:
    data = generate("unit1", "user1")
    if data is None:
        print("Error")
    else:
        print(data)
        json_export.json_export("temp_data", data)
    countdown(5)
    
