import subprocess
import os


try:
    choice = int(input("Nombre de qr code à créer > "))
except:
    print("erreur un nombre est requis")


for i in range(int(choice)):

    proccess = subprocess.Popen(["python", "./server.py", "no", str(i)])
os.system("cls")
#, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT
