from kasutaja import Kasutaja

class Admin(Kasutaja):
    privileegid = []

    def naita_privileegid(self):
        print(self.privileegid)
        