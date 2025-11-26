def soma():
    resultado = primeiroNumero + segundoNumero
    return resultado

def subtracao():
    resultado = primeiroNumero - segundoNumero
    return resultado

def Divisao():
    resultado = primeiroNumero / segundoNumero
    return resultado


def Multiplicacao():
    resultado = primeiroNumero * segundoNumero
    return resultado

def Calculadora():
    global primeiroNumero
    global segundoNumero

    while True:
        print()
        print("===============")
        print("||Calculadora||")
        print("===============")
        print()
        print(" 1 - soma\n 2 - subtracao\n 3 - Divisao\n 4 - Multiplicacao\n 0 - Sair\n")
        escolha = int(input("Qual a sua Escolha? "))
        if escolha == 0:
            break
        else:
            primeiroNumero = float(input("\nQual o primeiro numero: "))
            segundoNumero = float(input("\nQual o segundo numero: "))
            if escolha == 1:
                resultado = soma()
                operador = '+'
            elif escolha == 2:
                resultado = subtracao()
                operador = '-'
            elif escolha == 3:
                if segundoNumero == 0:
                    print("\nO segundo nao pode ser igual a zero!")
                    return
                else:
                    resultado = Divisao()
                    operador = '/'
            elif escolha == 4:
                resultado = Multiplicacao()
                operador = 'x'

        print(f"\nConta: {primeiroNumero:.2f} {operador} {segundoNumero:.2f} = {resultado:.2f}")
        input('\nEnter para continuar.')

Calculadora()

#eu levei sabe se lá quantos minutos para fazer este código