from tkinter import *
#three interesting facts you didnt need to know, first up i touch kids at 2am, number 2 i accidentaly sell body parts online because im an unemployed, number 3 i kicked microsoft workers balls at 5 am

def Teste():
    print("teste")
    print("lalala minha cabeça está piscando... lalala... lalala")

takeAShowerBro= Tk()
takeAShowerBro.title("take a Shower and touch grass bro")
takeAShowerBro.geometry('500x350+100+200')
takeAShowerBro.wm_resizable(width=True, height=True)

button = Button(takeAShowerBro, text="click here to take a shower", command= Teste, font="Time 10 bold")
button.place(width= 250, height= 40, x= 100, y= 50)

letHimCook=Label(takeAShowerBro, text='Teste', font='Time 10 bold')
letHimCook.place(width=80, height=40, x=10, y=40)

testTwo = Button(takeAShowerBro, text="click here to touch grass", command= Teste, font="Time 10 bold")
testTwo.place(width= 250, height= 40, x= 100, y= 100)

letHimCook2=Label(takeAShowerBro, text='lol', font='Time 10 bold')
letHimCook2.place(width=80, height=40, x=350, y=40)

lordSexIMeanX=Label(takeAShowerBro, text='lord se- i mean x', font='Time 10 bold')
lordSexIMeanX.place(width=120, height=40, x=165, y=10)

takeAShowerBro.mainloop()