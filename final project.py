#eyes-watching-from-the-darkness-scary-stories-120cbdacf74c
import tkinter as ttk
from tkinter import messagebox
from time import sleep
from tkinter import *
from tkinter import messagebox
import os
import folium
from PIL import Image, ImageTk
import requests
from datetime import datetime
from io import BytesIO
import tkinter as tk

def ClicaBotao(index):
    global jogadorAtual, board, buttons
    if board[index] == '':
        board[index] = jogadorAtual
        buttons[index].config(text=jogadorAtual)
        if VerificaVencedor():
            messagebox.showinfo("Fim de jogo lol lol lol lol lol lol", f"jogador {jogadorAtual} venceu karai!")
            sleep(5)
            abrir_nova_janela()
            Reset()
        elif '' not in board:
            messagebox.showinfo("Fim do jogo","Empate")
            sleep(5)
            imagemPatch = "eyes-watching-from-the-darkness-scary-stories.png"

            Reset()
        else:
            if jogadorAtual == 'X':
                jogadorAtual = '0'
            else:
                jogadorAtual = 'X'

def VerificaVencedor():
    combinacoes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for comb in combinacoes:
        if board[comb[0]] == board[comb[1]] == board[comb[2]] != '':
            return True
    return False

def Reset():
    global board, buttons, jogadorAtual
    board = ['' for _ in range(9)]
    for button in buttons:
        button.config(text='')
    jogadorAtual = 'X'

if __name__ == "__main__":
    root = tk.Tk()
    root.title("jogo do galo")

    jogadorAtual = 'X'
    board = ['' for _ in range(9)]
    buttons = []


    for i in range(9):
        button = tk.Button(root, text='', font=('normal', 40), width= 5, height= 2, command=lambda i=i: ClicaBotao(i))
        button.grid(row=i//3, column=i%3)
        buttons.append(button)

def abrir_nova_janela():
    nova_janela = tk.Toplevel(root)
    nova_janela.title("peso em tkinter")
    nova_janela.geometry("250x150")
    
    # Adicionando um texto na nova janela
    label = ttk.Label(nova_janela, text="Esta é a nova janela!")
    label.pack(pady=20)


caminhoDoScript = os.path.dirname(os.path.abspath(__file__))
os.chdir(caminhoDoScript)

def calculoImc():
    try:
        peso = float(entryPeso.get())
        altura = float(entryAltura.get()) / 100
        imc = peso / (altura ** 2)
        labelResultado.config(text= f"O teu peso é de {imc:.2f}Kg/m2")

        if imc < 18.5:
            imagemPath = "imc_magro.png"
        elif imc < 24.9:
            imagemPath = "imc_normal.png"
        elif imc < 29.9:
            imagemPath = "imc_sobrepeso.png"
        elif imc < 39.9:
            imagemPath = "imc_obeso.png"
        else:
            imagemPath = "imc_obeso2.png"

        imagem = PhotoImage(file=imagemPath)
        labelImagem.config(image=imagem)
        labelImagem.image = imagem

    except ValueError:
        messagebox.showerror("Erro", "Por favor insira valores válidos para peso e altura!")


janela = Tk()
janela.title('Calculadora de IMC')

framePrincipal = Frame(janela, padx=20, pady=20)
framePrincipal.pack()

labelTitulo = Label(framePrincipal, text='Calculadora de IMC', font=("Arial", 18))
labelTitulo.grid(row=0, column=0, columnspan=2, pady=10)

labelPeso = Label(framePrincipal, text='Peso (kg):')
labelPeso.grid(row=1, column=0, pady=5, sticky="w")
entryPeso = Entry(framePrincipal, width=10)
entryPeso.grid(row=1, column=1, pady=5)

labelAltura = Label(framePrincipal, text="Altura (cm):")
labelAltura.grid(row=2, column=0, pady=5, sticky="w")
entryAltura = Entry(framePrincipal, width=10)
entryAltura.grid(row=2, column=1, pady=5)

buttonCalcular = Button(framePrincipal, text="Calcular IMC", command=calculoImc)
buttonCalcular.grid(row=3, column=0, columnspan=2, pady=10)

labelResultado = Label(framePrincipal, text="", font=("Arial", 14))
labelResultado.grid(row=4, column=0, columnspan=2, pady=10)

labelImagem = Label(framePrincipal)
labelImagem.grid(row=5, column=0, columnspan=2)

labelImagem = sleep(10)

abrir_nova_janela()

def abrir_nova_janela():
    nova_janela = tk.Toplevel(root)
    nova_janela.title("mapa Portugal")
    nova_janela.geometry("250x150")
    
    # Adicionando um texto na nova janela
    label = ttk.Label(nova_janela, text="Esta é a nova janela!")
    label.pack(pady=20)

latitude = 39.3999
longitude = -8.2245

mapaPortugal = folium.Map(location=[latitude, longitude], zoom_start=6)

folium.Marker(
    location=[38.7167, -9.139],
    popup='Lisboa',
    icon=folium.Icon(icon='cloud')
).add_to(mapaPortugal)

folium.Marker(
    location=[41.1579, -8.6291],
    popup='Porto',
    icon=folium.Icon(icon='green')
).add_to(mapaPortugal)

mapaPortugal.save('mapaPortugal.html')

sleep(5)
tk.Toplevel

API_KEY = "3b3ddc5f98b8f6502b43eea92f40a73d"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
ICON_URL = "http://openweathermap.org/img/wn/"

def obterDadosMeteorologicos(cidade):
    params = {
        'q': cidade,
        'appid': API_KEY,
        'units': 'metric',
        'lang': 'pt'
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()


def guardarHistorico(cidade, temperatura):
    with open('historicoTemperaturas.txt', 'a', encoding='utf-8') as ficheiro:
        dataHora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ficheiro.write(f"{dataHora} - {cidade}: {temperatura}°C\n")

class AppMeteorologia:

    def __init__(self, janela):
        self.janela = janela
        self.janela.title("App de Meteorologia")
        self.janela.geometry("400x300")
        self.janela.configure(bg="#2E2E2E")

        self.cidadeLabel = tk.Label(janela, text="Cidade / País:", bg="#2E2E2E", fg="white")
        self.cidadeLabel.pack(pady=10)

        self.cidadeEntry = tk.Entry(janela, width=50)
        self.cidadeEntry.pack(pady=10)

        self.buscarButton = tk.Button(janela, text="Pesquisar", command=self.procurarMeteorologia, bg="white")
        self.buscarButton.pack(pady=10)

        self.resultadoLabel = tk.Label(janela, text="", wraplength=350, bg="#2E2E2E", fg="white")
        self.resultadoLabel.pack(pady=10)

        self.iconLabel = tk.Label(janela, bg="#2E2E2E")
        self.iconLabel.pack(pady=10)

    def procurarMeteorologia(self):
        cidade = self.cidadeEntry.get()
        if cidade:
            dados = obterDadosMeteorologicos(cidade)
            if dados.get("cod") != 200:
                messagebox.showerror("Erro", dados.get("message", "Erro ao procurar dados"))
            else:
                temperatura = dados["main"]["temp"]
                descricao = dados["weather"][0]["description"]
                iconCode = dados["weather"][0]["icon"]
                iconUrl = f"{ICON_URL}{iconCode}@2x.png"

                # Download da imagem do ícone
                response = requests.get(iconUrl)
                imgData = response.content
                img = Image.open(BytesIO(imgData))
                img = img.resize((100, 100), Image.LANCZOS)

                # Cria uma nova imagem com fundo cinza escuro
                background = Image.new('RGBA', img.size, (46, 46, 46, 255))
                img = Image.alpha_composite(background, img.convert('RGBA'))

                imgTk = ImageTk.PhotoImage(img)

                # Atualiza o ícone na interface
                self.iconLabel.config(image=imgTk)
                self.iconLabel.image = imgTk

                self.resultadoLabel.config(text=f"Temperatura: {temperatura}°C\nDescrição: {descricao.capitalize()}")
                guardarHistorico(cidade, temperatura)
        else:
            messagebox.showerror("Erro", "Por favor, insira o nome de uma cidade")


root.mainloop()