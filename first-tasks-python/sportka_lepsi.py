def losovat():
    losovani = []
    import random
    for i in range(1, 7):
        nahodne_cislo = random.randrange(1, 49)
        losovani.append(nahodne_cislo)
    print("Vylosovana cisla: {}".format(losovani))
    return losovani
def hadat():
    pokusy = []
    for i in range(1, 7):
        pokus = int(input("Vloz {}. cislo:".format(i)))
        pokusy.append(pokus)
    return pokusy

def porovnat(losovani, pokusy):
    shodna_cisla = []
    for i in range(6):
        if pokusy[i] in losovani:
            shodna_cisla.append(pokusy[i])
    print("Vsazena cisla: {}".format(pokusy))
    print("Vylosovana cisla: {}".format(losovani))
    print("Uhodnuta cisla: {}".format(shodna_cisla))


def sportka():
    losovani = losovat()
    pokusy = hadat()
    porovnat(losovani, pokusy)

if __name__ == "__main__":
    sportka()
