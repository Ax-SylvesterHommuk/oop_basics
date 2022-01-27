from sodur_inimene import Sodur
from random import randint

armee1 = []
armee1_id = []
armee2 = []
armee2_id = []

for i in range(1, 21):
    armee_valik = randint(1, 2)
    if armee_valik == 1:
        armee1.append(Sodur(armee_valik))
    else:
        armee2.append(Sodur(armee_valik))

for sodur in armee1:
    armee1_id.append(sodur.id)

for sodur in armee2:
    armee2_id.append(sodur.id)

print("Esimeses armees on sõdurid IDs: " + ', '.join(map(str, armee1_id)))
print("Tesises armees on sõdurid IDs: " + ', '.join(map(str, armee2_id)))