import json

def json_export(filename, data):
	with open(filename + ".json", "w") as write_file:
		json.dump(data, write_file)