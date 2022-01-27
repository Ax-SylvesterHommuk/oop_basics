class Inimene():
    def __init__(self, eesnimi, perenimi, kutse_kval = 1):
        self.eeenimi = eesnimi
        self.perenimi = perenimi
        self.kutse_kval = kutse_kval
    def tutvustus(self):
        print("Tere, olen,", self.eeenimi,self.perenimi)
    def __del__(self):
        print("Tervitused!")