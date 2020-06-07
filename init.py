import requests
import json


token = "8edc82295a38d66040fc9160517e805e5438ff4e"
url = "https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token={}".format(token)

r = requests.get(url)

f = open("answer.json", "w")
f.write(json.dumps(r.json()))
f.close()

text = r.json().get('cifrado')
rules = ['.', ' ']

for i in range(len(text)):
    if text[i] not in rules:
        print(chr(ord(text[i]) - 3), end='')
    print(text[i], end='')
