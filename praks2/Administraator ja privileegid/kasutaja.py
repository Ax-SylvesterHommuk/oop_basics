class Kasutaja():
    def __init__(self, e_nimi, p_nimi, s_kats = 0):
        self.eesnimi = e_nimi
        self.perenimi = p_nimi
        self.sisse_katse = s_kats

    def setandmed(self, age, mail):
        self.email = mail
        self.vanus = age

    def kirjelda_kasutaja(self):
        print("Kasutaja eesnimi on {0}, perenimi on {1}, vanus on {2} ja email on {3}".format(self.eesnimi, self.perenimi, self.vanus, self.email))

    def tervita_kasutaja(self):
        print("Tervitan kasutajat {0}, sisselogimised: {1}".format(self.eesnimi, self.sisse_katse))

    def suurenda_sisselogimiskatsed(self):
        self.sisse_katse += 1

    def reset_sisselogimiskatsed(self):
        self.sisse_katse = 0
