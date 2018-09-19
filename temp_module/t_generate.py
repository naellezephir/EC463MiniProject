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
