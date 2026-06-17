#eyes-watching-from-the-darkness-scary-stories-120cbdacf74c
import tkinter as tk
from tkinter import messagebox, ttk
import random
import folium
import requests
import os
from datetime import datetime
from PIL import Image, ImageTk
from io import BytesIO
from time import sleep

API_KEY = "3b3ddc5f98b8f6502b43eea92f40a73d"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
ICON_URL = "http://openweathermap.org/img/wn/"
caminhoDoScript = os.path.dirname(os.path.abspath(__file__))
os.chdir(caminhoDoScript)

def limparJanela():
    for widget in janela.winfo_children():
        widget.destroy()

board = ['' for _ in range(9)]
buttons = []

def jogoDoGalo():
    limparJanela()
    janela.title("Jogo do Galo")

    tk.Label(janela, text='Ganha ao Computador!', font=("Arial", 14)).pack(pady=10)

    areaJogo = tk.Frame(janela)
    areaJogo.pack()

    global board, buttons
    board = ['' for _ in range(9)]
    buttons = []

    for i in range(9):
        button = tk.Button(areaJogo, text='', font=('normal', 40), width= 5, height= 2, command=lambda i=i: ClicaBotao(i))
        button.grid(row=i//3, column=i%3)
        buttons.append(button)

def ClicaBotao(index):
    global board, buttons

    if board[index] == '':

        board[index] = "X"
        buttons[index].config(text="X")

        if VerificaVencedor():
            messagebox.showinfo("Fim de jogo lol lol lol lol lol lol", f"Venceu karai!")
            limparJanela()
            labelImagem = tk.Label(janela)
            # if os.path.exists("transferir.jpg"):
            #     imagem = tk.PhotoImage(file="transferir.jpg")
            #     labelImagem.config(image=imagem)
            #     labelImagem.image = imagem
            #     sleep(4)
            imc()
            return
        espacos_vazios = []
        for i in range(9):
            if board[1] == '':
                espacos_vazios.append(i)

        if espacos_vazios:
            jogadas_pc = random.choice(espacos_vazios)
            board[jogadas_pc] = '0'
            buttons[jogadas_pc].config(text='0')

            if VerificaVencedor():
                messagebox.showinfo("Fim de jogo", "O Computador venceu! Tenta de novo.")
                Reset()

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
    global board
    board = ['' for _ in range(9)]
    for button in buttons:
        button.config(text='')

def imc():
    limparJanela()
    janela.title("TUA SAUDE.EXE FR FR")

    tk.Label(janela, text='Calcular o teu IMC de baleia', font=("Arial", 16)).pack(pady=10)

    tk.Label(janela, text='Peso (kg):').pack()
    entryPeso = tk.Entry(janela)
    entryPeso.pack(pady=5)

    tk.Label(janela, text="Altura (cm):").pack()
    entryAltura = tk.Entry(janela)
    entryAltura.pack(pady=5)
    

    # labelResultado = tk.Label(janela, text="", font=("Arial", 14))
    # labelResultado.pack(pady=5)

    # labelImagem = tk.Label(janela)
    # labelImagem.pack(pady=5)


    def calcularImc():
        try:
            peso = float(entryPeso.get())
            altura = float(entryAltura.get()) / 100
            imc = peso / (altura ** 2)
            #labelResultado.config(text= f"O teu peso é de {imc:.2f}Kg/m2")

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

            imagem = tk.PhotoImage(file=imagemPath)
            # labelImagem.config(image=imagem)
            # labelImagem.image = imagem

        except ValueError:
            messagebox.showerror("Erro", "Por favor insira valores válidos para peso e altura!")
            
    tk.Button(janela, text="calcular e avançar", command=calcularImc, bg="blue").pack(pady=5)

def meteorologia():
    limparJanela()
    janela.title("Meteorologiainator")

    tk.Label(janela, text='Como está o tempo belo senhor?', font=("Arial", 16)).pack(pady=10)

    tk.Label(janela, text='qual cidade?').pack()
    entryCidade = tk.Entry(janela)
    entryCidade.pack(pady=5)

    resultadoLabel = tk.Label(janela, text="", wraplength=350, bg="#2E2E2E", fg="white")
    resultadoLabel.pack(pady=10)

    iconLabel = tk.Label(janela, bg="#2E2E2E")
    iconLabel.pack(pady=10)

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

    def verOTempo():
        cidade = entryCidade.get()
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
                iconLabel.config(image=imgTk)
                iconLabel.image = imgTk
                mensagem = f"Temperatura: {temperatura}°C\nDescrição: {descricao.capitalize()}"
                resultadoLabel.config(text=mensagem)
                guardarHistorico(cidade, temperatura)
                messagebox.showinfo("Tempo Atual", mensagem)
                criarMapa()

        else:
            messagebox.showerror("Erro", "Por favor, insira o nome de uma cidade")

    buscarButton = tk.Button(janela, text="Pesquisar", command=verOTempo, bg="white")
    buscarButton.pack(pady=10)

def criarMapa():
    limparJanela()
    janela.title("fazedor de mapas")

    tk.Label(janela, text='Faz o teu mapa desempregado', font=("Arial", 16)).pack(pady=10)

    cidades = ["porto", "lisboa", "faro", "Coimbra"]
    listaEscolha = ttk.Combobox(janela, values= cidades, state="readonly")
    listaEscolha.set("porto")
    listaEscolha.pack(pady=10)

    def fazerMapa():
        escolha = listaEscolha.get()

        if escolha == "porto":
            coordenadas = [41.1579, -8.6291]
        elif escolha == "lisboa":
            coordenadas = [38.7167, -9.1390]
        elif escolha == "faro":
            coordenadas = [37.0194, -7.9322]
        else:
            coordenadas = [40.2056, -8.4195]

        mapaPortugal = folium.Map(location=coordenadas, zoom_start=6)
        folium.Marker(
            location=coordenadas,
            popup=escolha
        ).add_to(mapaPortugal)

        mapaPortugal.save('mapaPortugal.html')

        messagebox.showinfo("parabens", "já criaste um mapa")
        janela.destroy()

    buscarButton = tk.Button(janela, text="Pesquisar", command=fazerMapa, bg="white")
    buscarButton.pack(pady=10)

janela = tk.Tk()
janela.geometry("400x500")

jogoDoGalo()

janela.mainloop()

