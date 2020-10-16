mondat = "ez itt egy szoveg jjjjjj"


def gyakori_betuk(szoveg):
    # itt csinalok a szovegbol egy szokozok nelkuli betukbol allo listat:
    betuk = list(szoveg.replace(" ", ""))
    gyujtemeny = {}
    # ha a gyujtemenyben benne van mar a betu, akkor az elofordulasi erteket megnovelem
    # ha nincs benne, akkor beleteszem
    for betu in betuk:
        if betu not in gyujtemeny:
            gyujtemeny[betu] = 1
        else:
            gyujtemeny[betu] += 1
    # ertekek alapjan rendezem a dictionaryt:
    rendezett_gyujtemeny = sorted(
        gyujtemeny.items(), key=lambda x: x[1], reverse=True)

    leggyakoribb_harom_betu = []
    for betu in rendezett_gyujtemeny[0:3]:
        leggyakoribb_harom_betu.append(betu[0])

    return leggyakoribb_harom_betu


print(gyakori_betuk(mondat))
