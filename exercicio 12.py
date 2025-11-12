euro = int(input("quantos euros queres converter? "))
print()
print('''Qual moeda deseja converter:
[0] Real Brasileiro
[1] Bath Tailandes''')
moeda=int(input('Escolha a sua opção: '))
real=6.34*euro
bath=37.90*euro
print()
if moeda==0:
    print('Isso lhe dará', real, 'Reais Brasileiros')
else:
    print('isso lhe dará', bath, 'em bath Tailandes')