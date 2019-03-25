#!/usr/bin/env python3
import sys
import argparse

#parser dos atributos vindos do terminal
parser = argparse.ArgumentParser(description='Cifra um texto usando a cifra de caesar.')
parser.add_argument('-c', '--cifra', metavar=('texto-aberto.txt','texto-cifrado.txt'), 
    nargs=2, help='Flag para cifrar uma mensagem.')
parser.add_argument('-d', '--decifra', metavar=('texto-cifrado.txt','texto-aberto.txt'), 
    nargs=2, help='Flag para decifrar uma mensagem.')
parser.add_argument('-k', '--key', metavar='chave', type=int, nargs=1, 
    help='Chave para cifrar/decifrar.')

#alfabeto completo com os codigos ascii das letras ([A-Z] + [a-z] + [0-9]), no formato de lista
alfabeto = list(range(65, 91)) + list(range(97, 123)) + list(range(48, 58))
ALFABETO_LENGTH = len(alfabeto)

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

#cifra de cesar, recebe uma mensagem e 'desloca' cada um dos caracteres n vezes, determinado pela chave
def cifra(mensagem, chave):
    chave %= ALFABETO_LENGTH
    mensagem_cifrada = ''
    for char in mensagem:
        if ord(char) in alfabeto:
            index = alfabeto.index(ord(char))
            mensagem_cifrada += chr(alfabeto[(index + chave) % ALFABETO_LENGTH])
        else:
            mensagem_cifrada += char
    return mensagem_cifrada

#decifra a mensagem negativando a chave e aplicando a cifra novamente
def decifra(mensagem, chave):
    return cifra(mensagem, -chave)

#'le' os atributos passados pelo terminal
args = parser.parse_args()

#se -c e chave, cifra o texto
#(args.cifra[0] = texto-aberto, args.cifra[1] = texto-cifrado)
if args.cifra and args.key:
    mensagem = abre_txt(args.cifra[0])
    mensagem_cifrada = cifra(mensagem, args.key[0])
    cria_txt(args.cifra[1], mensagem_cifrada)

#se -d e chave, decifra o texto 
#(args.cifra[0] = texto-cifrado, args.cifra[1] = texto-aberto)
if args.decifra and args.key:
    mensagem_cifrada = abre_txt(args.decifra[0])
    mensagem_decifrada = decifra(mensagem_cifrada, args.key[0])
    cria_txt(args.decifra[1], mensagem_decifrada)
