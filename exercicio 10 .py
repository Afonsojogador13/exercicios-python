velocidade = float(input("A que velocidade o teu veiculo vai? "))

if velocidade > 120:
    sensor_inteligente = (velocidade - 120)*4
    sla = f"A multa que tens que pagar são: {sensor_inteligente:.2f}€"
elif velocidade > 80:
    sensor_inteligente = (velocidade - 80)*2
    sla = f"A multa que tens que pagar são: {sensor_inteligente:.2f}€"
elif velocidade == 80:
    sla = "quase ultapassavas o limite de velocidade"
else:
    sla = "A tua velocidade é inferior a 80"

print(sla)