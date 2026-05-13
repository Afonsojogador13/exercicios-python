from tkinter import *
from tkinter import messagebox

branco = "#ffffff"
azul = "#364a85"
vermelho = "#b53128"
amarelo = "#ffef08"

janela = Tk()
janela.title('Agenda')
janela.geometry('380x650+500+100')
janela.wm_resizable(width=False, height=False)

labelAgenda = Label(janela, text='Sharkcoders Python', font='Time 20 bold', bg=amarelo, fg=vermelho, anchor='w', padx=10)
labelAgenda.place(width=380, height=50, x=0, y=0)

labelNome = Label(janela, text='Nome', font='Time 10', anchor='w')
labelNome.place(width=60, height=20, x=10, y=70)
inputNome = Entry(janela, font='Time 10')
inputNome.place(width=250, height=20, x=100, y=70)

labelTelefone = Label(janela, text='telefone', font='Time 10', anchor='w')
labelTelefone.place(width=60, height=20, x=10, y=105)
inputTelefone = Entry(janela, font='Time 10')
inputTelefone.place(width=250, height=20, x=100, y=105)

labelEndereço = Label(janela, text='endereço', font='Time 10', anchor='w')
labelEndereço.place(width=60, height=20, x=10, y=140)
inputEndereço = Entry(janela, font='Time 10')
inputEndereço.place(width=250, height=20, x=100, y=140)

labelDistrito = Label(janela, text='distrito', font='Time 10', anchor='w')
labelDistrito.place(width=60, height=20, x=10, y=175)
inputDistrito = Entry(janela, font='Time 10')
inputDistrito.place(width=105, height=20, x=100, y=175)

labelPais = Label(janela, text='país', font='Time 10', anchor='w')
labelPais.place(width=60, height=20, x=230, y=175)
inputPais = Entry(janela, font='Time 10')
inputPais.place(width=80, height=20, x=270, y=175)

labelEmail = Label(janela, text='Email', font='Time 10', anchor='w')
labelEmail.place(width=60, height=20, x=10, y=210)
inputEmail = Entry(janela, font='Time 10')
inputEmail.place(width=250, height=20, x=100, y=210)

def ReceberEntries():
    nome = inputNome.get()
    telefone = inputTelefone.get()
    endereço = inputEndereço.get()
    distrito = inputDistrito.get()
    pais = inputPais.get()
    email = inputEmail.get()

    return nome,telefone,endereço,distrito,pais,email

def LimparEntries():
    inputNome.delete('0', 'end')
    inputTelefone.delete('0', 'end')
    inputEndereço.delete('0', 'end')
    inputDistrito.delete('0', 'end')
    inputPais.delete('0', 'end')
    inputEmail.delete('0', 'end')

def Adicionar():
    nome, telefone, endereço, distrito, pais, email = ReceberEntries()
    
    with open('agenda.txt', 'a') as arquivo:
        arquivo.write(nome + '\n' + telefone + '\n' + endereço + '\n' + distrito + '\n' + pais + '\n' + email + '\n')

    messagebox.showinfo('Agenda','Cadastro Efetuado com sucesso!')

    LimparEntries()

def Procurar():
    pNome = inputNome.get()
    with open('agenda.txt', 'r') as arquivo:
        for linha in arquivo:
            if pNome in linha:
                pTelefone = (arquivo.readline())
                pEndereço = (arquivo.readline())
                pDistrito = (arquivo.readline())
                pPais = (arquivo.readline())
                pEmail = (arquivo.readline())

                labelNomeBusca = Label(janela, text=linha, font='Times 10 bold', anchor='w')
                labelNomeBusca.place(width=250, height=30, x=20, y=360)
                labelTelefoneBusca = Label(janela, text=pTelefone, font='Times 10 bold', anchor='w')
                labelTelefoneBusca.place(width=250, height=30, x=20, y=380)
                labelEndereçoBusca = Label(janela, text=pEndereço, font='Times 10 bold', anchor='w')
                labelEndereçoBusca.place(width=250, height=30, x=20, y=400)
                labelDistritoBusca = Label(janela, text=pDistrito, font='Times 10 bold', anchor='w')
                labelDistritoBusca.place(width=250, height=30, x=20, y=420)
                labelPaisBusca = Label(janela, text=pPais, font='Times 10 bold', anchor='w')
                labelPaisBusca.place(width=250, height=30, x=20, y=440)
                labelEmailBusca = Label(janela, text=pEmail, font='Times 10 bold', anchor='w')
                labelEmailBusca.place(width=250, height=30, x=20, y=460)
                LimparEntries()
                messagebox.showinfo('Agenda', 'Cadastro encontrado!')
            else:
                messagebox.showerror('Agenda', 'Cadastro não encontrado!')
                break

buttonAdicionar = Button(janela, text='Adicionar', command=Adicionar, font='Time 10 bold', bg=azul, fg=branco)
buttonAdicionar.place(width=80, height=30, x=70, y=310)

buttonProcurar = Button(janela, text='Pesquisar', command=Procurar, font='Time 10 bold', bg=azul, fg=branco)
buttonProcurar.place(width=80, height=30, x=240, y=310)

janela.mainloop()
