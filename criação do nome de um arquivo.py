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

def Menu():
    Cabecalho("criação de texto")
    SubCabecalho("Menu")
    escolha = int(input(" 1 - criar ficheiro \n 2 - Conteúdo do Ficheiro \n 3 - Ler Ficheiro \n 4 - Encontrar palavra \n 0 - Sair \n\n Escolha: "))
    
    return escolha

def UtilizadorNomeFicheiro():
    global nomeFicheiro
    nomeFicheiro = input("qual o nome do ficheiro: ")

def NomeFicheiro():
    UtilizadorNomeFicheiro()
    open(f'{nomeFicheiro}.txt', 'w', encoding='utf-8')
    
    print(f'"{nomeFicheiro}.txt" aberto com sucesso')
    input("\n\nEnter Para Inicar") 

def UtilizadorConteudoFicheiro():
    global conteudoFicheiro
    conteudoFicheiro = input("Agora escreve o conteudo deste ficheiro: ")

def ConteudoFicheiro():
    UtilizadorConteudoFicheiro()
    with open(f'{nomeFicheiro}.txt', 'a', encoding='utf-8') as file:
        file.write(conteudoFicheiro)
    print(f'Conteudo ({conteudoFicheiro}) foi adicionado ao ficheiro "{nomeFicheiro}.txt" com sucesso!')
    input("\n\nEnter Para Inicar")

def UtilizadorLerFicheiro():
    pergunta = input("\nQuer ler o ficheiro? Sim(S), Não(N): ")

    if pergunta.upper() == "S":
        return True
   
    return False

def LerFicheiro():
    pergunta = UtilizadorLerFicheiro()
    if pergunta:
        with open(f"{nomeFicheiro}.txt", "r", encoding='utf-8') as file:
            ficheiro = file.read()
            print(ficheiro)
    else:
        print("Terminado")
    input("\n\nEnter Para Inicar")

def ProcuraDaPalavra():
    global palavra
    palavra = input("Qual palavra deseja procurar: ")

def EncontrarPalavra():
    ProcuraDaPalavra()
    with open(f"{nomeFicheiro}.txt", "r", encoding='utf-8') as file:
        for linha in file:
            if palavra in linha:
                print(linha.rstrip())
                print(f"palavra {palavra} encontrada")
            else:
                print(f'Palavra "{palavra}" não encontrado(a)')
    input("\n\nEnter Para Inicar")

def Ficheiro():
    Cabecalho("Ficheiro")
    input("\n\nEnter Para Inicar")
    while True:
        Cabecalho("Ficheiro")
        escolha = Menu()
        Limpar()
        if escolha == 0:
            SubCabecalho("Sayonara".upper())
            break
        elif escolha == 1:
            NomeFicheiro()
        elif escolha == 2:
            ConteudoFicheiro()
        elif escolha == 3:
            LerFicheiro()
        elif escolha == 4:
            EncontrarPalavra()
        else:
            SubCabecalho("Escolha nao valida!")

Ficheiro()
