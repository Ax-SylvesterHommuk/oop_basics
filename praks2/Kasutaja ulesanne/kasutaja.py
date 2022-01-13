class Kasutaja():
    eesnimi = ""
    perenimi = ""
    vanus = 0

    def kirjelda_kasutaja(self):
        print("Kasutaja eesnimi on {0}, perenimi on {1} ja vanus on {2}".format(self.eesnimi, self.perenimi, self.vanus))

    def tervita_kasutaja(self):
        print("Tervitan kasutajat {0}".format(self.eesnimi))