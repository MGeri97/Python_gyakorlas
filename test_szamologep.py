"""
Tesztek a szamologep.py modulhoz
"""

from szamologep import (hatvanyozas, kivonas, kor_terulet, osszeadas, osztas,
                        szorzas)


def test_osszeadas():
    """Teszt az összeadás funkcióhoz"""
    assert osszeadas(2, 3) == 5
    assert osszeadas(-1, 1) == 0
    assert osszeadas(0, 0) == 0


def test_kivonas():
    """Teszt a kivonás funkcióhoz"""
    assert kivonas(5, 3) == 2
    assert kivonas(0, 5) == -5
    assert kivonas(10, 10) == 0


def test_szorzas():
    """Teszt a szorzás funkcióhoz"""
    assert szorzas(3, 4) == 12
    assert szorzas(-2, 3) == -6
    assert szorzas(0, 100) == 0


def test_osztas():
    """Teszt az osztás funkcióhoz"""
    assert osztas(10, 2) == 5.0
    assert osztas(7, 2) == 3.5
    assert osztas(-6, 3) == -2.0


def test_osztas_nullaval():
    """Teszt az osztás nullával funkcióhoz"""
    try:
        osztas(5, 0)
        assert False, "Null osztás nem váltott ki hibát"
    except ZeroDivisionError:
        assert True


def test_hatvanyozas():
    """Teszt a hatványozás funkcióhoz"""
    assert hatvanyozas(2, 3) == 8
    assert hatvanyozas(5, 0) == 1
    assert hatvanyozas(3, 2) == 9


def test_kor_terulet():
    """Teszt a kör területének kiszámítása funkcióhoz"""
    from math import pi

    assert kor_terulet(1) == pi * 1 * 1
    assert kor_terulet(0) == 0
    assert kor_terulet(2.5) == pi * 2.5 * 2.5


if __name__ == "__main__":
    test_osszeadas()
    test_kivonas()
    test_szorzas()
    test_osztas()
    test_osztas_nullaval()
    print("Minden teszt sikeres!")
