massa = float(input("qual é o seu peso em kilogramas?: "))
altura = float(input("Qual é a sua altura em centrimetros?: ")) / 100

imc = massa / (altura ** 2)

print(f"o teu peso é de {imc:.2f}Kg/m2")