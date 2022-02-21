from opimine import Andmed
from opimine import Õpetaja
from opimine import Õpilane

# Andmed() lubab endasse jätta meelde erinevaid teemasid.
teemad = Andmed("klass", "objekt", "pärilus", "polümorfism", "kalseldus")
anna = Õpetaja()
kadi = Õpilane()
mati = Õpilane()

# Klass Õpilane() lubab õpilasel erinevaid teemasid õppida.
mati.õpib(teemad[0])
mati.õpib(teemad[1])
mati.õpib(teemad[2])
mati.õpib(teemad[3])
mati.unusta()
