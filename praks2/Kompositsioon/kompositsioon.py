from tuba import Tuba

tuba = Tuba(int(input("Sisestage toa pikkus:")), int(input("Sisestage toa laius:")), int(input("Sisestage toa korgus:")))


tuba.lisa_Aknad_uks(int(input("Sisestage ukse laius:")), int(input("Sisestage ukse kõrgus:")))


valik = input("Kas toas on aknaid? jah/ei : ").lower()


while valik == "jah":
    tuba.lisa_Aknad_uks(int(input("Sisestage akna laius:")), int(input("Sisestage akna korgus:")))
    valik = input("Kas toas on veel aknaid? jah/ei : ").lower()


tuba.tapeedi_rull(int(input("Sisestage tapeedi rulli laius: ")), int(input("Sisestage tapeedi rulli pikkus: ")))
print("Tapeeti on vaja {0} m2, mis on {1} rulli".format(tuba.toopindala(), round(tuba.tapeedi_rulle)))