from aknad_ja_uksed import Aknad_ja_Uksed

class Tuba():

    def __init__(self, pikkus, laius, korgus):
        self.aknad_uksed = []
        self.pikkus = pikkus
        self.laius = laius
        self.korgus = korgus

    def pindalad(self, pikkus, laius, korgus):
        pindala = 2 * korgus * (pikkus + laius)
        return pindala

    def tapeedi_rull(self,pikkus,laius):
        self.tapeedi_rulli = pikkus * laius
        self.tapeedi_rulle = self.toopindala() / self.tapeedi_rulli

    def lisa_Aknad_uks(self, au_laius, au_korgus):
        self.aknad_uksed.append(Aknad_ja_Uksed(au_laius, au_korgus))

    def toopindala(self):
        uus_pindala = self.pindalad(self.pikkus, self.laius, self.korgus)
        for element in self.aknad_uksed:
            uus_pindala = uus_pindala - element.pindala
        return uus_pindala