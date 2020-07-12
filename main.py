def log(rem):
    import datetime
    rem=rem[:-4]
    with open("mylogs.txt",'a') as f:
        f.writelines("\n"+str(rem)+"\t-------"+str(str(datetime.datetime.now())))
def play(rem):
    from pygame import mixer
    while True:
        mixer.init()
        mixer.music.load(rem)
        mixer.music.play()
        x=input("inplay for x")
        if x=='stop':
            log(rem)
            break
        elif x=='e':
            break


def wait():
    from time import time
    initeye=initexe=initdri=time()
    x='s'
    while x!='e':
        # x = input("wait ip")
        time()
        if time()-initdri>drisec:
            initdri = time()
            play("Drink.mp3")

        elif time() - initeye > eyesec:
            initeye = time()
            play(("Eye.mp3"))

        elif time()-initexe>exesec:
            initexe = time()
            play("Exercise.mp3")

if __name__ == '__main__':
    print("This program is for healthy programming"
          "in which you will get reminder to do"
          "healthy activities")
    print("Enter 'stop' to stop reminder")
    x=input("Enter s for start and e for quit at any time ")
    exesec=50
    drisec=5
    eyesec=15
    wait()

