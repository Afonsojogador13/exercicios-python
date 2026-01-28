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

Cabecalho("Afonso")
input("Enter para Continuar")
Cabecalho("Professor David")