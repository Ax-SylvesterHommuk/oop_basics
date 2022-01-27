class Restoraan():
    def __init__(self, r_nimi, s_tuup):
        self.restoraani_nimi = r_nimi
        self.soogi_tyyp = s_tuup

    def kirjelda_restoraan(self):
        print("Restorani nimi: " + self.restoraani_nimi)
        print("Restorani Sook: " + self.soogi_tyyp)

    def ava_restoraan(self):
        print("Restoraan " + self.restoraani_nimi + " on avatud!")