# -*- coding: UTF-8 -*-
import requests
import json
import hashlib


TOKEN = "8edc82295a38d66040fc9160517e805e5438ff4e"
URL = "https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token={}".format(TOKEN)
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
ROT = 3


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
    return hashlib.sha1(content)


def request():
    return requests.get(URL)


def main():
    text = request().json()
    manage_file(json.dumps(text))

    text['decifrado'] = cipher(text.get('cifrado'))

    manage_file(json.dumps(text))

    text['resumo_criptografico'] = create_hash(text.get('decifrado'))

    manage_file(json.dumps(text))


main()
