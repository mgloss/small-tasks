shodna_cisla = []
pokusy = []
losovani = []
def losovat():
    import random
    for i in range(1, 7):
        nahodne_cislo = random.randrange(1, 49)
        losovani.append(nahodne_cislo)
    print("Vylosovana cisla: {}".format(losovani))
def hadat():
    for i in range(1, 7):
        pokus = int(input("Vloz {}. cislo:".format(i)))
        pokusy.append(pokus)

def porovnat():
    for i in range(6):
        if pokusy[i] in losovani:
            shodna_cisla.append(pokusy[i])
    print("Vsazena cisla: {}".format(pokusy))
    print("Vylosovana cisla: {}".format(losovani))
    print("Uhodnuta cisla: {}".format(shodna_cisla))



def sportka():
    losovat()
    hadat()
    porovnat()

sportka()
