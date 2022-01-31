class Restoraan():
    def __init__(self, r_nimi, s_tuup):
        self.restoraani_nimi = r_nimi
        self.soogi_tyyp = s_tuup

    teen_kyl = 0

    def kirjelda_restoran(self):
        kirj_tekst = self.restoraani_nimi + " pakub " + self.soogi_tyyp
        print(kirj_tekst)

    def maara_teenindatud_kyl(self, kyl_arv):
        self.teen_kyl = kyl_arv

    def suurenda_teen_kyl(self, suur_kyl_arv):
        self.teen_kyl += suur_kyl_arv

    def ava_restoraan(self):
        print(self.restoraani_nimi + " on avatud")