class Kasutaja():
    def __init__(self, e_nimi, p_nimi,):
        self.eesnimi = e_nimi
        self.perenimi = p_nimi

    def setandmed(self, age, mail):
        self.email = mail
        self.vanus = age

    def kirjelda_kasutaja(self):
        print("Kasutaja eesnimi on {0}, perenimi on {1}, vanus on {2} ja email on {3}".format(self.eesnimi, self.perenimi, self.vanus, self.email))

    def tervita_kasutaja(self):
        print("Tervitan kasutajat {0}".format(self.eesnimi))