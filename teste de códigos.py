from time import sleep
import os

listaNormal = ["steve hawking","lol","hypno","jazzghost","tissa","gaybriel"]
listaDaInsanidade = ["angel gabby","angel zaggy","francis","angel cammy"]
def Limpar():
    os.system("cls")

def Cabecalho(texto):
    Limpar()
    tamanho = len(texto) + 6
    print()
    print("="*tamanho)
    print(f"|| {texto} ||")
    print("="*tamanho)
    print()

def Nome():
    global nome
    while True:
        Cabecalho("Diz qualquer nome")
        nome = input("Nome: ")

        input("Enter para Continuar")

        if nome.lower() in listaNormal:
            print(f"noooosssa {nome}")
            print("que bom nome")
            sleep(2)
        elif nome.lower() in listaDaInsanidade:
            print("    ......        ......    ")
            print("  .. 0000 ..    .. 0000 ..  ")
            print("    ......        ......    ")
            print("                            ")
            print("      \              /      ")
            print("       --------------       ")
            sleep(2)
            Quiz()
        else:
            print("idk")
            sleep(2)
  
            break

def Quiz():
    Cabecalho(f"{nome} Vais fazer Quiz")
    idade = int(input("coloca uma idade: "))

    if idade >= 10:
        print("hmmm, acho que alguém vai explodir")
    elif idade >= 30:
        print("porque é que estás aqui hein?")
        sleep(5)
        print("sai")
        sleep(0.5)
        print("daqui")
        sleep(0.5)
        print("agora")
    else:
        print("idade desconhecida, mas não importa")

    resposta = input("estás pronto ou pronta?: ")
    if resposta.lower() == "yes":
        print("ok então vamos começar o QUIZZZZZZZZZZZZZZZZZZZZZZZZZZZ")
        sleep(6)
        PerguntasDoQuiz()
    else:
        print("0   0")
        print(" \_/ ")

def PerguntasDoQuiz():
    Cabecalho("qual opção está correta?")
    print("a angel gabby é...")
    listaCorreta = 0
    listaErrada = ["1","2","3"]
    sleep(1)
    print("opção 1: um anjo da guarda")
    sleep(1)
    print("opção 2: um coelho")
    sleep(1)
    print("opção 3: uma personagem ficticia")
    sleep(1)
    opções = int(input(" "))
    if opções == listaCorreta:
        print(".")
        sleep(0.1)
        print(".")
        sleep(0.1)
        print(".")
        sleep(2)
        print("como é que tu sabias que ela era uma ###############?")
        sleep(1)
        print("enfim vamos para a próxima pergunta")
        sleep(4)
        QuizDois()
    elif opções in listaErrada:
        print(f"falhaste {nome}, agora vais explodir")
        sleep(0.5)
        print("*sons de explosões explodidas, mas agora em um Quiz fr fr*")
        sleep(7)
    else:
        print("Opção Invalida, tenta novamente!")
        sleep(4)
        PerguntasDoQuiz()

def QuizDois():
    Cabecalho("qual é a resposta correta?")
    print("quanto é 49341646 + 94446466?")
    listaCorretaDois= 2
    listaErradaDois= ["1", "3"]
    sleep(1)
    print("opção 1: 213214234")
    sleep(1)
    print("opção 2: 143788112")
    sleep(1)
    print("opção 3: idk, man im going to play fortnite")
    sleep(1)
    opçõesDois = int(input(" "))
    if opçõesDois == listaCorretaDois:
        print("és um génio ou uma génia da matemática")
        sleep(1)
        print("enfim, vamos para o último quiz")
        sleep(2)
        QuizTres()
    elif opçõesDois in listaErradaDois:
        print(f"falhaste {nome}, agora vais explodir")
        sleep(0.5)
        print("*sons de explosões explodidas, mas agora no segundo Quiz fr fr*")
        sleep(7)
    else:
        print("resposta inválida, tente novamente")
        sleep(5)
        QuizDois()
def QuizTres():
    Cabecalho("o que preferes sofrer")
    UltimaListaCorreta= 1
    UltimaListaErrada= 2
    sleep(3) #bro got slept, and i ate your doorframe
    print("opção 1: ser torturado ou torturada pelo executável, cuja a identidade não será revelada")
    sleep(5)
    print("opção 2: trabalhar de CLT")
    sleep(3)
    UltimaOpção = int(input(" "))
    if UltimaOpção == 1:
        print("drowning")
        sleep(1)
        print("drowning")
        sleep(1)
        print("sinking")
        sleep(1)
        print("sinking")
        sleep(1)
        print("ok, já chega o jogo acabou...")
        sleep(7)
    elif UltimaOpção == 2:
        print("finalmente perdeste, agora serás explodido")
        sleep(3)
        print("*sons de explosões explodidas extremitas*")
        sleep(2)
    else:
        print("isso não é uma opção...")
        sleep(2)
        print("adeus")

Nome()
Quiz()
QuizDois()
QuizTres()