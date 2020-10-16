class Allat:
    # private
    __in_zoo = 0
    # protected
    _species = None

    def __init__(self, species):
        self.add_newanimal(self)
        self._species = species

    @staticmethod
    def add_newanimal(self):
        self.__in_zoo += 1


morzsi = Allat('kutya')
# eleri, protected
print(morzsi._species)

# nem eri el, privat: hiba
# print(morzsi.__in_zoo)


class Gimnazium:
    def __init__(self, nev):
        self.nev = nev


kosztolanyi = Gimnazium("Kosztolanyi")
kosztolanyi.cim = "Budapest"
print(kosztolanyi.cim)
