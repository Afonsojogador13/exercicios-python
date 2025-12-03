from random import randint

def SeisESeis():
    contador = 0
    while True:
        contador += 1
        dadoUm = randint(1,6)
        dadoDois = randint(3,6)
        print(f'Dado 1: {dadoUm} / Dado 2: {dadoDois}\n')
        if (dadoUm == 6) and (dadoDois == 6):
            print(f"ambos os numeros calharam no 6, e foram necessárias: {contador} vezes para isso acontecer")  
            break

SeisESeis()
