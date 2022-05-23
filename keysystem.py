#i want a girlfriend so bad..
#im so lonely..
import time
import random
import string
import os
import pickle
import os.path
from colorama import init, Fore
init(convert=True)
import subprocess, requests


#saves ur key
def keyexposing():  
    print(f"{Fore.GREEN}We have your key in the system, now we just need to save it in a file and you are done! ")
    pickle.dump(key, open("yourkey.dat", "wb"))


#generates ur key
def keygenerate(size=15, chars=string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))

#variable to save the function
key = keygenerate()


#main function where main code will be stored
def main():
    print("yay u made it!")

#checking if key is in system
def checkingkey():
    if os.path.exists('yourkey.dat'):
        main()
    else:
        print("you dont have a key, imma exit now, bye! :D")
        time.sleep(1)
        exit(123)

#activating all the stuff above :D
def keysystem():
    keyexposing()
    time.sleep(1)
    checkingkey()



keysystem()