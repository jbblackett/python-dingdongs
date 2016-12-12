#Works if ethernet in bridge
#Makes post requests to IFTTT - would be faster with phue

import requests

print("Welcome")
print()
print("1. Turn off light")
print("2. Turn on light")
print("3. Set light brightness")

while True:
    option = ""
    while not ((option == "1") or (option == "2") or (option == "3")):
        option = input("Please enter a number: ")
    if option == "1":
        r = requests.post("https://maker.ifttt.com/trigger/lightoff/with/key/HzW4Sk-C8fkYJ5UhkuJCv")
    elif option == "2":
        r = requests.post("https://maker.ifttt.com/trigger/light/with/key/HzW4Sk-C8fkYJ5UhkuJCv", data = {"value1" : "100", "value2" : "null", "value3" : "null"})
    elif option == "3":
        brightness = 101
        while not ((int(brightness) >= 0) and (int(brightness) <= 100)):
            brightness = input("Brightness percentage: ")
        values = {"value1" : brightness, "value2" : "null", "value3" : "null"}
        url = "https://maker.ifttt.com/trigger/light/with/key/HzW4Sk-C8fkYJ5UhkuJCv"
        r = requests.post(url, data = values)
    print()
