from tkinter import *
white = "#d6d6d6"
blue = "#3341e6"
red = "#e00b39"
yellow = "#d9e00b"
green = "#0be018"

def Blue():
    janela.configure(bg=blue)
    labelColor.configure(text="Blue", bg=blue)

def Red():
    janela.configure(bg=red)
    labelColor.configure(text="Red", bg=red)

def Yellow():
    janela.configure(bg=yellow)
    labelColor.configure(text="Yellow", bg=yellow)

def Green():
    janela.configure(bg=green)
    labelColor.configure(text="Green", bg=green)

    

janela = Tk()
janela.title('color changer')
janela.geometry('500x500+560+120')
janela.wm_resizable(width=False, height=False)
janela.configure(background = white)

buttonBlue = Button(janela, text='Azul', command=Blue, font='Time 14 bold', bg=blue)
buttonBlue.place(width=200, height=160, x=40, y=20)

buttonRed = Button(janela, text='Vermelho', command=Red, font='Time 14 bold', bg=red)
buttonRed.place(width=200, height=160, x=260, y=20)

buttonYellow = Button(janela, text='amarelo', command=Yellow, font='Time 14 bold', bg=yellow)
buttonYellow.place(width=200, height=160, x=40, y=200)

buttonGreen = Button(janela, text='verde', command=Green, font='Time 14 bold', bg=green)
buttonGreen.place(width=200, height=160, x=260, y=200)

labelColor = Label(janela, text='colour', font='Time 20 bold', bg=white)
labelColor.place(width=120, height=60, x=190, y=390)

janela.mainloop()