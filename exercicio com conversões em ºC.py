def fahrToCelsius(temp):
    iCanSeeYou = ((temp - 32) * (5/9))
    return iCanSeeYou

def Temperatura():
    temperatura = float(input("Coloca um número, mais espesificamente em temp. fahrenheit"))

    conversao = fahrToCelsius(temperatura)

    print(f"{conversao:.2f}ºC")

for x in range(1, 6):
    Temperatura()