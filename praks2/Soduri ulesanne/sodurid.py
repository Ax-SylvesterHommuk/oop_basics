from sodur import Sodur
from random import randint

sodur1 = Sodur()
sodur2 = Sodur()

while (sodur1.tervis > 0 and sodur2.tervis > 0):
    x_hit = randint(1, 2)
    if (x_hit == 1):
        print("Esimene lööb teist")
        sodur2.tervis -= 20
    elif(x_hit == 2):
        print("Teine lööb esimest")
        sodur1.tervis -= 20

if (sodur1.tervis != 0):
    print("Esimene võitis!")
    print("Teine kaotas.")
else:
    print("Teine võitis.")
    print("Esimene kaotas.")
