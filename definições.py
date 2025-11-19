def quantasLetrasTem():
    soma = 0
    frase = input("Entre com a frase: ")
    findHim = input("Qual letra deseja verificar: ")
    for elemento in frase:
        if elemento == findHim:
            soma += 1
    print(f'Nesta frase aparece {soma} vezes a letra ({findHim}).')

quantasLetrasTem()
