from random import randint

class Andmed():
    def __init__(self, *info):
        self.info = list(info)

    def __getitem__(self, i):
        return print(self.info[i])

class Õpetaja():
    # Õpetab grupp inimesi ühe korraga.
    def õpetab(self, info, *õpilane):
        for i in õpilane:
            i.õpib(info)

class Õpilane():
    def __init__(self):
        self.teadmised = []

    def õpib(self, info):
        self.teadmised.append(info)

    # Lubab õpilasel ise õppida ilma Õpib() meetodiga.
    def õpibise(self, info):
        self.õpib(info)

    # Juhuslikult valib erinevad teema mida õpilane unustab.
    def unusta(self):
        listi_len = len(self.teadmised)
        ununeb = randint(0, listi_len)
        print("Mul läks meelest ära teema: " + str(self.teadmised[ununeb]))
        self.teadmised.pop(ununeb)
