"""
Tesztek a szamologep.py modulhoz
"""

from szamologep import kivonas, osszeadas, osztas, szorzas, hatvanyozas


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


if __name__ == "__main__":
    test_osszeadas()
    test_kivonas()
    test_szorzas()
    test_osztas()
    test_osztas_nullaval()
    print("Minden teszt sikeres!")
