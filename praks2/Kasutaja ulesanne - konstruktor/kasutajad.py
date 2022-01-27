from kasutaja import Kasutaja

kasutaja1 = Kasutaja("Ax-Sylvester","Hommuk")
kasutaja2 = Kasutaja("Sander", "Hera")
kasutaja3 = Kasutaja("Hendri", "Nõmmik")

kasutaja1.setandmed(17, "ax-sylvester.hommuk@voco.ee")
kasutaja2.setandmed(17, "sander.hera@voco.ee")
kasutaja3.setandmed(17, "hendri.nõmmik@voco.ee")

kasutaja1.tervita_kasutaja()
kasutaja1.kirjelda_kasutaja()

kasutaja2.tervita_kasutaja()
kasutaja2.kirjelda_kasutaja()

kasutaja3.tervita_kasutaja()
kasutaja3.kirjelda_kasutaja()