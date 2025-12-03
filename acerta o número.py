from random import randint

#vai para o scratch ver a minha conta manfonso4
def Numeros():
    numeroSecreto = randint(1,100)
    contador = 0    


    print("Escolha o número entre 1 e 100")
    print()

    while True:
        contador +=1
        escolha = int(input("Qual o numero? Digita pelo seu palpite "))
        if numeroSecreto > escolha:
            print('Errado! O número é maior que seu pa- quero dizer o seu número') #kkkkkkkkkkkkkkkkkkkk
        elif numeroSecreto < escolha:
            print('Exageraste só um pouco no número')
        else:
            print("Correct :)")
            break

        
    print('Foram necessárias',contador,'jogadas')


Numeros()