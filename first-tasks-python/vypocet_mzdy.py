def vypocet_superhruba_mzda(supehruba_mzda):
    superhruba_mzda = hruba_mzda + (hruba_mzda * 0.34)
    return superhruba_mzda

def vypocet_pojisteni(hruba_mzda):
    pojisteni = hruba_mzda * 0.11
    return pojisteni

def vypocet_dan(superhruba_mzda):
    dan = superhruba_mzda * 0.15
    return dan

def vypocet_zaloha(dan):
    zaloha = dan - 2070
    if zaloha < 0:
        return 0
    else:
        return zaloha

def vypocet_cista_mzda(hruba_mzda):
    cista_mzda = hruba_mzda - pojisteni - zaloha
    return cista_mzda

hruba_mzda = int(input("Zadej hrubou mzdu: "))
superhruba_mzda = vypocet_superhruba_mzda(hruba_mzda)
pojisteni = vypocet_pojisteni(hruba_mzda)
dan = vypocet_dan(superhruba_mzda)
zaloha = vypocet_zaloha(dan)
cista_mzda = vypocet_cista_mzda(hruba_mzda)


print("Vase hruba mzda je %d." % hruba_mzda)
print("Vase superhruba mzda je %d." % superhruba_mzda)
print("Vase vydaje na pojisteni jsou %d." % pojisteni)
print("Vase dan je %d." % dan)
print("Zaloha na dan je %d." % zaloha)
print("Vase cista mzda je %d." % cista_mzda)
if hruba_mzda > vypocet_cista_mzda(29320):
    print("Vase mzda je vyssi nez prumerna.")
elif hruba_mzda < vypocet_cista_mzda(29320):
    print("Vase mzda je nizsi nez prumerna.")
else:
    print("Vase mzda je prumerna.")




