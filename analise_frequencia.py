#!/usr/bin/env python3
import sys

alfabeto = list(range(ord('A'), ord('Z'))) + list(range(ord('a'), ord('z'))) + list(range(ord('0'), ord('9')))


#abre o txt e retorna o seu conteudo, caso sucesso
def abre_txt(arquivo):
    try:
        file = open(arquivo, 'r')
        mensagem = file.read()
        file.close()
        return mensagem
    except:
        sys.exit('Nao foi possivel abrir o arquivo ' + arquivo)

caracteres = {}
mensagem = list(abre_txt(sys.argv[1]))

for char in mensagem:
    if char not in caracteres:
        caracteres.update({char:1})
    else:
        caracteres[char] += 1

numero_caracteres = sum(caracteres.values())
caracteres = dict(sorted(caracteres.items(), key=lambda x: x[1], reverse = True))

for char in caracteres:
    freq = caracteres[char]
    print(char + ' - ' + str(freq) + ' - ' + "%.2f" % ((freq/numero_caracteres)*100) + '%')

index = 0
for char in caracteres:
    if ord(char) in alfabeto:
        index = ord(char)
        break

print('Logo, a chave da cifra deve ser: ' + str(alfabeto.index(index) - alfabeto.index(ord('a'))))
