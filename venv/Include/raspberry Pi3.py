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
    print("values: ", value)
    for x in value:
        if x == '0':
            print("人工控制")
        if x == '1':
            print("自动控制")
        if x == '1001':
            print("Air Conditioner On!")
        if x == '1002':
            print("Air Conditioner Off!")
        if x == '1003':
            print("Humidifier On")
        if x == '1004':
            print("Humidifier Off")
        if x == '1005':
            print("Light On")
        if x == '1006':
            print("Light Off!")
        if x == '1007':
            print("Windows Off!")
        if x == '1008':
            print("Windows Off!")
    time.sleep(5)









