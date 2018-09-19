import time

import json_export
from t_generate import generate

# Timer Def
def countdown(t):
	while t:
		time.sleep(1)
		t -= 1
while True:
    data = generate("unit1", "user1")
    if data is None:
        print("Error, data generation failed")
    else:
        print(data)
        json_export.json_export("temp_data", data)
    countdown(5)
