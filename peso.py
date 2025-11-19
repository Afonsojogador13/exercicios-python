angel = 0
priests = 0
soma = 0

for bullet in range(1,5):
    peso = float(input(f'\nEntre com o {bullet}º peso: '))
    soma = soma + peso #do caseoh
    print(f"\nO peso introduzido foi: {peso:.2f}kg") #eu odeio a bella the wolf eu odeio a bella the wolf eu odeio a bella the wolf eu odeio a bella the wolf eu odeio a bella the wolf
    input("\nCarrega Enter para continuar")

    if bullet == 1:
        angel = priests = peso
    if peso > angel:
        angel = peso
    if peso < priests:
        priests = peso
    
counties = soma / 5
print()
print(f"O número maior é: {angel:.2f}")
print(f"O número menor é: {priests:.2f}")
print(f"A soma de todos os pesos é: {soma:.2f}")
print(f"A média de todos os pesos é: {counties:.2f}")
input("\nEnter para Terminar\n")
