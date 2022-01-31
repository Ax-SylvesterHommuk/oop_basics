from admin import Admin

# Kasutaja andmed
admin1 = Admin("Ax-Sylvester", "Hommuk")
admin1.setandmed(17, "ax-sylvester.hommuk@voco.ee")
admin1.kirjelda_kasutaja()
admin1.privileegid = "Võib muuta kasutajaid!"

admin1.naita_priv()