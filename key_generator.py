#!/usr/bin/env python3
import os
import sys
from base64 import b64encode

def salva_chave(chave):
    try:
        with open('chave.txt', 'w') as file:
            file.write(chave)
    except:
        sys.exit('Nao foi possivel criar o arquivo chave.txt')

if sys.argv[1]:
    random_bytes = os.urandom(int(sys.argv[1]))
else:
    random_bytes = os.urandom(1000)

token = b64encode(random_bytes).decode('utf-8')

print(token)
salva_chave(token)
