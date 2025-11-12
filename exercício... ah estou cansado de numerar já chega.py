dindin = int(input("qual o salário do trabalhor que deseja? "))
print()
if dindin < 500:
    reajuste = 15
elif dindin <= 1000:
    reajuste = 10
else:
     reajuste = 5
im_stuck_in_the_oven = dindin * reajuste / 100
novo_salário = dindin + im_stuck_in_the_oven
print("o novo salário é", novo_salário)
print(f"\nO reajuste será de {reajuste}%")
print(f"O aumento será de {im_stuck_in_the_oven:.2f}$")
print(f"O novo salário passará para {novo_salário:.2f}")