from kasutaja import Kasutaja # Kasutan pythoni faili mis oli eelmine kord tehtud.

class Admin(Kasutaja):
    privileegid = ""

    def naita_priv(self):
        print(self.privileegid)
