import requests
import json

from os import listdir

properties = ""
smartplug_api_params = "./smartplug/"

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
    return data


def get_request_parameters(command):
    for file in listdir(smartplug_api_params):
        if file.find(command, 0, len(command)) == 0:
            with open(smartplug_api_params+file, 'r') as json_params:
                data = json.load(json_params)
    return data


def post_request(command):
    global properties
    ip = ""
    for p in properties:
        p = p.split("=")
        if p[0] == "ip":
            ip = p[1]

    data = get_request_parameters(command)

    response = requests.post("http://" + ip + '/' + command, data)

    return


def smartplug_setup(filename):
    global properties
    properties = open(filename, "r")


if __name__ == '__main__':
    print(get_request_parameters('sta'))
