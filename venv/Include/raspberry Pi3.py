import os, io, sys, re, time, base64, json
import webbrowser, urllib.request

while(True):
    url = "http://localhost:9091/Raspberry"
    stdout = urllib.request.urlopen(url)
    ControlResource = stdout.read().decode('utf-8')
    jsonData = json.loads(ControlResource)
    key = list(jsonData["data"].keys())
    value = list(jsonData["data"].values())
    print("keys: ", key)
    if key == ['control_mode']:
        data = value[0];
        print("data: ", data)
    time.sleep(5)









