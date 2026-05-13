from time import sleep
from random import randint
import os

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
    
def SubCabecalho(texto):
    print()
    print(f"### {texto} ###")
    print()

def Cadastro():
    nome = input("Qual nome deseja procurar?: ")
    idade = int(input('Entre com a idade: '))
    with open("Lista_Idades.txt", "r", encoding="utf-8") as file:
        file.write(f'{nome}\n')
        file.write(f'{str(idade)}\n')
        

def EncontrarNome():
    palavra = input("Qual nome deseja procurar: ")
    with open("Lista_Idades.txt", "r", encoding='utf-8') as arquivo:
        conteudo = arquivo.readlines()
    encontrado = False

    for linha in range(len(conteudo)):
        if palavra.lower() in conteudo[linha].lower():
            print(f"\n\n Nome: {conteudo[linha].strip()}")

            if linha + 1 < len(conteudo):
                print(f"\n\n Idade: {conteudo[linha + 1].strip()}")

            encontrado = True
            print("-" * 20)
    
    if not encontrado:
        print("Nome não encontrado!")

    input("\n\n Enter Para Inicar")

def Menu():
    Cabecalho("criação de texto")
    SubCabecalho("Menu")
    escolha = int(input(" 1 - cadastrar-se \n 2 - encontrar palavra \n 0 - Sair(lol) \n\n Escolha: "))
    
    return escolha

def Ficheiro():
    Cabecalho("Ficheiro")
    input("\n\n Enter Para Inicar")
    while True:
        escolha = Menu()
        Limpar()
        if escolha == 0:
            SubCabecalho("Sayonara".upper())
            break
        elif escolha == 1:
            Cadastro()
        elif escolha == 2:
            EncontrarNome()
        else:
            SubCabecalho("Escolha não válida!")

Ficheiro()