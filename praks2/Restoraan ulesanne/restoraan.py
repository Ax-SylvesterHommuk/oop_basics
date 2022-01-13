class Restoraan():
    restoraani_nimi = ""
    soogi_tyyp = ""

    def kirjelda_restoraan(self):
        print("Restorani nimi: " + self.restoraani_nimi)
        print("Restorani Sook: " + self.soogi_tyyp)

    def ava_restoraan(self):
        print("Restoraan " + self.restoraani_nimi + " on avatud!")