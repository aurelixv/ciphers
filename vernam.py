#!/usr/bin/env python3
import sys

#abre o txt e retorna o seu conteudo, caso sucesso
def abre_txt(arquivo):
    try:
        file = open(arquivo, 'r')
        mensagem = file.read()
        file.close()
        return mensagem
    except:
        sys.exit('Nao foi possivel abrir o arquivo ' + arquivo)

#cria um txt com o nome passado por arquivo e escreve a mensagem
def cria_txt(arquivo, mensagem):
    try:
        file = open(arquivo, 'w')
        file.write(mensagem)
        file.close()
    except:
        sys.exit('Nao foi possivel criar o arquivo ' + arquivo)

def vernam(mensagem, chave):
    i = 0
    mensagem_cifrada = ""
    for char in mensagem:
        if i >= len(chave):
            i = 0
        mensagem_cifrada += chr(ord(char) ^ ord(chave[i]))
        i += 1
    return mensagem_cifrada

mensagem = abre_txt('vernam-cifrada.txt')
chave = abre_txt('chave.txt')

mensagem_cifrada = vernam(mensagem, chave)

cria_txt('vernam-cifrada.txt', mensagem_cifrada)
