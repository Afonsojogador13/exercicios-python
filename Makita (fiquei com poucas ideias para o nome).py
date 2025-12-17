from time import sleep

#only jerks mess with fireworks
def Countdown():
    stopPunctuation = int(input("qual a contagem decrescente?"))
    
    while True:
        if stopPunctuation == 0:
            print("BIG SHOT")
            break
        else:
            print(stopPunctuation)
            stopPunctuation -= 1
            sleep(1)

Countdown()