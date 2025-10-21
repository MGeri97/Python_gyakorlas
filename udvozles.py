# Ez egy felhasználói üdvözlő program. Bekéri a felhasználó nevét, majd üdvözli őt.


def udvozles():
    nev = input("Kérem, adja meg a nevét: ")
    print(f"Üdvözlöm, {nev}!")


if __name__ == "__main__":
    udvozles()
