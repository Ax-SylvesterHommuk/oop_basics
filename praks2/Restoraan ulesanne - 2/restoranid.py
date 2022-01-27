from restoraan import Restoraan

restoran1 = Restoraan("Hendri Restoraan", "Kana")

restoran1.kirjelda_restoran()
restoran1.ava_restoraan()

print(restoran1.teen_kyl)
restoran1.maara_teenindatud_kyl(20)

print(restoran1.teen_kyl)
restoran1.suurenda_teen_kyl(20)

print(restoran1.teen_kyl)