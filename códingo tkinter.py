from tkinter import *

root = Tk()
root.title('test')
root.geometry('500x350+100+200')
root.wm_resizable(width=True, height=True)

def Ola():
    tituloLabel = Label(root, text="Janela de Teste", font="Time 16 bold", bg= '#364a85', fg= '#ffffff', anchor='c', padx=10)
    tituloLabel.pack(fill='x', side='top', ipady=15)

botaoOla = Button(root, text='Ola', command=Ola, font='Time 10 bold', bg= '#364a85', fg= '#ffffff', anchor="c")
botaoOla.place(width=100, height=40, x=200, y=120)

root.mainloop()