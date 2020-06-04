import requests
import json

properties = ""


def get_request(command="status"):
    global properties
    ip = ""
    for p in properties:
        p = p.split("=")
        if p[0] == "ip":
            ip = p[1]
    response = requests.get("http://" + ip + '/' + command)
    data = json.loads(response.text)
    print(json.dumps(json.dumps(data, indent=4, sort_keys=True)))


def smartplug_setup(filename):
    global properties
    properties = open(filename, "r")
