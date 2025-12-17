from random import randint

def HiOrLo():
    contador = 0
    numeroSecreto = randint(1,100)
    while True:
        contador += 1
        adivinha = int(input("tenta adivinhar o número secreto "))
        #ill watch as you ### for i warnedd you and warned you and you did not meat~
        if adivinha > numeroSecreto:
            print(f"numero secreto é menor do que {adivinha}")
        elif adivinha < numeroSecreto:
            print(f"numero secreto é maior do que {adivinha}")
        else:
            print("parabéns, parabéns, parabéns, parabéns, parabéns, conseguiste")
            print(f"O numero secreto é {numeroSecreto}!")
            print(f"Demoraste {contador} vezes para adivinhar!")
            break

HiOrLo() 