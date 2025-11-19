inicial = int(input("Escolha o número inicial: "))
final = int(input("Escolha o numero final: "))
incremento = int(input("Escolha o valor de incremento: "))

print(f"\nOs números entre {inicial} e {final}, com um incremento de {incremento}, sao:")

for numero in range(inicial, final +1, incremento):
    print()
    print(numero, end=" ")

print()
print("Enter para terminar")
