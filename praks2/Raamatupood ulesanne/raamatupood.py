class Raamatupood():

    def __init__(self, nimi, reiting):
        self.nimi = nimi
        self.reiting = reiting
        self.raamatu_list = []

    def saan_lisada_raamat(self, pealkiri, reiting):
        self.raamat = pealkiri

        if pealkiri not in self.raamatu_list == True:
            if reiting >= self.reiting:
                print("Raamatut saab lisada!")

    def lisa_raamat(self, pealkiri, autor, hind, reiting):
        if (pealkiri in self.raamatu_list):
            print("See raamat on juba poes.")
        else:
            raamat_dict = {"pealkiri": pealkiri, "autor": autor, "hind": hind, "reiting": reiting}
            self.raamatu_list.append(raamat_dict)
            print(f"Lisasid raamatu: {pealkiri}")

    def saan_eemaldada_raamat(self, pealkiri):
        for i in self.raamatu_list:
            if i["pealkiri"] == pealkiri:
                print(f"Seda raamatut on võimalik ära eemaldada ({pealkiri})")

    def eemalda_raamat(self, pealkiri):
        if (pealkiri in self.raamatu_list):
            self.raamatu_list.remove(f"{pealkiri}")
            print(f"Eemaldasid raamatu: {pealkiri}")

    def naita_koik_raamatud(self):
        for i in self.raamatu_list:
            print(i["pealkiri"])

    def naita_raamatud_hinna_jargi(self):
        pass

    def naita_koige_populaarsem_raamat(self):
        pass
