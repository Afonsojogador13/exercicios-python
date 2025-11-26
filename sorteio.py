#driving in my car right a beer hey that bump is shaped like a deer DUI...
import random

soma = 0
numerosSorteados = []

def PrimeiroSorteio():
    #"V1"
    # contador = 1
    #while contador <= 10
        #numero = random.randint(1, 100)
        #numerosSorteados.append(numero)
        #contador += 1

#"v2"
    for i in range(1, 11):
        numero = random.randint(1, 100)
        numerosSorteados.append(numero)

    print(f"\nOs 10 valores sorteados foram: {numerosSorteados}\n")

def SomaDosNumerosDaLista():
    global soma

    for numero in numerosSorteados:
        if numero % 2 == 0:
            soma += numero

    print(f"A soma de todos os numeros dentro da lista e: {soma}\n")

PrimeiroSorteio()
SomaDosNumerosDaLista()