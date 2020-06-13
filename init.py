# -*- coding: UTF-8 -*-
import requests
import json
import hashlib


TOKEN = "8edc82295a38d66040fc9160517e805e5438ff4e"
URL = "https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token={}".format(TOKEN)
URL_POST = "https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token={}".format(TOKEN)
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
ROT = 7


def manage_file(content):
    f = open("answer.json", "w", encoding='utf-8')
    f.write(content)
    f.close()


def cipher(message):
    m = ''
    for c in message:
        if c in ALPHABET:
            c_index = ALPHABET.index(c)
            m += ALPHABET[(c_index + (-1 * ROT)) % len(ALPHABET)]
        else:
            m += c
    return m


def create_hash(content):
    return hashlib.sha1(str(content).encode('utf-8')).hexdigest()


def request():
    return requests.get(URL)


def request_post():

    answer = {"answer": open("answer.json", "rb")}
    r_post = requests.post(URL_POST, files=answer)

    print(r_post.text)


def main():
    text = request().json()
    manage_file(json.dumps(text))

    text['decifrado'] = cipher(text.get('cifrado'))

    manage_file(json.dumps(text))

    text['resumo_criptografico'] = create_hash(text.get('decifrado'))

    manage_file(json.dumps(text))

    request_post()


main()
