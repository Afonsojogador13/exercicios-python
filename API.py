import requests

lista = ['EUR', 'USD', 'BRL']

print('=-'*10)
print('Conversor de Moedas')
print('=-'*10)

de = int(input('Qual a moeda de origem?\n0 - Euro\n1 - Dolar Americano\n2 - Real brasileiro\nEscolha a opção: '))
de = lista[de]
print()
valor = int(input('Qual valor deseja converter: '))
print()
para = int(input('Para qual moeda deseja converter?\n0 - Euro\n1 - Dolar Americano\n2 - Real Brasileiro\nEscolha a opção: '))
para = lista[para]
print()

cotacao = requests.get(f'https://economia.awesomeapi.com.br/last/{de}-{para}')
cotacao = cotacao.json()
cotacaoMoeda = float(cotacao[f'{de}{para}']['bid'])

resultado = round(valor * cotacaoMoeda,2)
print(f'O valor convertido é de {resultado}{para}')


#https://smlwiki.com/

#XD