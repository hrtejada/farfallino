import re


def is_vovel(letter):
    return letter.lower() in 'aeiou'


def farfallino_transform(text):
    text_transformed = ''
    for char in text:
        text_transformed += '{}f{}'.format(char, char) if is_vovel(char) else char
    return text_transformed


def buscador_silabas(palabra):
    vocales = ['a', 'e', 'i', 'o', 'u']
    palabra_long = len(palabra)
    posiciones_silabas = []
    for i in range(palabra_long):
        caracter = palabra[i]
        siguiente_caracter = palabra[i+1] if i+1 < palabra_long else None
        if (caracter in vocales) and not (siguiente_caracter in vocales):
            posiciones_silabas.append(i)
    return posiciones_silabas

def traduce_a_f(palabra):
    pos_silabas = buscador_silabas(palabra)
    pafalafabrafa = palabra
    sumador_pos = 0
    for pos in pos_silabas:
        pafalafabrafa = pafalafabrafa[:pos+1+sumador_pos] + 'f' + palabra[pos] + pafalafabrafa[pos+1+sumador_pos:]
        sumador_pos += 2
    return pafalafabrafa