class AknadUksed:
    def __init__(self, laius, kõrgus):
        self.pindala = laius * kõrgus

class Tuba:
    def __init__(self, pikkus, laius, kõrgus):
        self.pindala = 2 * kõrgus * (pikkus + laius)
        self.aknad_uksed = []

    def lisaAkenUks(self, laius, kõrgus):
        self.aknad_uksed.append(AknadUksed(laius, kõrgus))

    def tööpind(self):
        uus_pindala = self.pindala

        for element in self.aknad_uksed:
            uus_pindala = uus_pindala - element.pindala
        return uus_pindala


tuba = Tuba(6 ,3, 2.7)
print(tuba.pindala)
tuba.lisaAkenUks(1, 1)
tuba.lisaAkenUks(1 ,1)
tuba.lisaAkenUks(1, 1)
print(tuba.tööpind())