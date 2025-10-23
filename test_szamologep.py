"""
Tesztek a szamologep.py modulhoz
"""

import math

from szamologep import (CalculatorMemory, cos, gyok, hatvanyozas, kivonas,
                        kor_kerulet, kor_terulet, log, log10, osszeadas,
                        osztas, sin, szorzas, tan)


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


def test_kor_kerulet():
    """Teszt a kör kerületének kiszámítása funkcióhoz"""
    from math import pi

    assert kor_kerulet(1) == 2 * pi * 1
    assert kor_kerulet(0) == 0
    assert kor_kerulet(2.5) == 2 * pi * 2.5


# Új funkciók tesztjei
def test_gyok():
    """Teszt a négyzetgyök funkcióhoz"""
    assert gyok(4) == 2.0
    assert gyok(9) == 3.0
    assert gyok(0) == 0.0
    assert abs(gyok(2) - 1.414213562) < 0.0001


def test_gyok_negativ():
    """Teszt a négyzetgyök negatív számmal"""
    try:
        gyok(-1)
        assert False, "Negatív szám gyöke nem váltott ki hibát"
    except ValueError:
        assert True


def test_sin():
    """Teszt a szinusz funkcióhoz"""
    assert abs(sin(0) - 0) < 0.0001
    assert abs(sin(math.pi / 2) - 1) < 0.0001
    assert abs(sin(math.pi) - 0) < 0.0001


def test_cos():
    """Teszt a koszinusz funkcióhoz"""
    assert abs(cos(0) - 1) < 0.0001
    assert abs(cos(math.pi / 2) - 0) < 0.0001
    assert abs(cos(math.pi) - (-1)) < 0.0001


def test_tan():
    """Teszt a tangens funkcióhoz"""
    assert abs(tan(0) - 0) < 0.0001
    assert abs(tan(math.pi / 4) - 1) < 0.0001


def test_log():
    """Teszt a természetes logaritmus funkcióhoz"""
    assert abs(log(1) - 0) < 0.0001
    assert abs(log(math.e) - 1) < 0.0001
    assert abs(log(math.e**2) - 2) < 0.0001


def test_log_negativ():
    """Teszt a logaritmus negatív számmal"""
    try:
        log(-1)
        assert False, "Negatív szám logaritmusa nem váltott ki hibát"
    except ValueError:
        assert True


def test_log10():
    """Teszt a 10-es alapú logaritmus funkcióhoz"""
    assert abs(log10(1) - 0) < 0.0001
    assert abs(log10(10) - 1) < 0.0001
    assert abs(log10(100) - 2) < 0.0001


def test_calculator_memory():
    """Teszt a memória funkciókhoz"""
    mem = CalculatorMemory()

    # Kezdeti állapot
    assert mem.memory_recall() == 0.0

    # Memóriába írás
    mem.memory_add(10)
    assert mem.memory_recall() == 10.0

    # További hozzáadás
    mem.memory_add(5)
    assert mem.memory_recall() == 15.0

    # Kivonás
    mem.memory_subtract(3)
    assert mem.memory_recall() == 12.0

    # Törlés
    mem.memory_clear()
    assert mem.memory_recall() == 0.0


def test_calculator_history():
    """Teszt az előzmények funkciókhoz"""
    mem = CalculatorMemory()

    # Kezdeti állapot
    assert len(mem.get_history()) == 0

    # Előzmény hozzáadása
    mem.add_history("5 + 3", 8, "10:00:00")
    assert len(mem.get_history()) == 1
    assert mem.get_history()[0] == ("5 + 3", 8, "10:00:00")

    # További előzmény
    mem.add_history("10 × 2", 20, "10:01:00")
    assert len(mem.get_history()) == 2

    # Előzmények törlése
    mem.clear_history()
    assert len(mem.get_history()) == 0


if __name__ == "__main__":
    test_osszeadas()
    test_kivonas()
    test_szorzas()
    test_osztas()
    test_osztas_nullaval()
    test_hatvanyozas()
    test_kor_terulet()
    test_kor_kerulet()
    test_gyok()
    test_sin()
    test_cos()
    test_tan()
    test_log()
    test_log10()
    test_calculator_memory()
    test_calculator_history()
    print("Minden teszt sikeres!")
