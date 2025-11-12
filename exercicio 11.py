numero_inicial = int(input("qual número queres dar ao primeiro resultado? "))
angel = int(input("ok, e qual número queres dar ao último? "))
# liar = int(input("Digite o incremento (passos): "))
print(f"Os números pares entre {numero_inicial} e {angel} são:")

for x in range(numero_inicial, angel+1):
    print("\nTodos")
    print(x)
    if x % 2 == 0:
        print("Os pares:")
        print(x, end=' ')
