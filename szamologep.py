# Importok végrehajtása
import math

PI = math.pi


# Alapvető matematikai műveletek
def osszeadas(a, b):
    """Két szám összeadása"""
    return a + b


def kivonas(a, b):
    """Két szám kivonása"""
    return a - b


def szorzas(a, b):
    """Két szám szorzása"""
    return a * b


def osztas(a, b):
    """Két szám osztása"""
    if b == 0:
        raise ZeroDivisionError("Nullával való osztás nem lehetséges.")
    return a / b


def hatvanyozas(a, b):
    """Két szám hatványozása"""
    return a**b


def kor_terulet(r):
    """Kör területének kiszámítása"""
    return PI * r * r


def kor_kerulet(r):
    """Kör kerületének kiszámítása"""
    return 2 * r * PI


# Két szám bekérése
def beolvas_szamok():
    a = float(input("Kérem az első számot (pontot használj tizedesjegyként!): "))
    b = float(input("Kérem a második számot (pontot használj tizedesjegyként!): "))
    return a, b


def utasitasok():
    print("Válassz műveletet:")
    print("1 - Összeadás")
    print("2 - Kivonás")
    print("3 - Szorzás")
    print("4 - Osztás")
    print("5 - Hatványozás")
    print("6 - Kör területének kiszámítása")
    print("7 - Kör kerületének kiszámítása")
    print("8 - Kilépés")


def main():
    while True:
        utasitasok()
        valasztas = input("Írd be a választott művelet számát (1/2/3/4/5/6/7/8): ")

        if valasztas == "8":
            print("Kilépés a programból.")
            break

        a, b = beolvas_szamok()

        if valasztas == "1":
            eredmeny = osszeadas(a, b)
            muvelet = "összeadás"
        elif valasztas == "2":
            eredmeny = kivonas(a, b)
            muvelet = "kivonás"
        elif valasztas == "3":
            eredmeny = szorzas(a, b)
            muvelet = "szorzás"
        elif valasztas == "4":
            try:
                eredmeny = osztas(a, b)
                muvelet = "osztás"
            except ZeroDivisionError as e:
                print(f"Hiba: {e}")
                continue
        elif valasztas == "5":
            eredmeny = hatvanyozas(a, b)
            muvelet = "hatványozás"
        elif valasztas == "6":
            eredmeny = kor_terulet(a)
            muvelet = "kör területe"
        elif valasztas == "7":
            eredmeny = 2 * a * PI
            muvelet = "kör kerülete"
        else:
            print("Érvénytelen választás. Kérlek próbáld újra.")
            continue

        print(f"A(z) {muvelet} eredménye: {eredmeny}")


if __name__ == "__main__":
    main()
