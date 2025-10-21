"""
Üdvözlő program tesztelése
"""

from udvozles import udvozles


def test_udvozles(nev):
    """Teszt az üdvözlő funkcióhoz"""
    assert udvozles(nev) == f"Üdvözlöm, {nev}!"


if __name__ == "__main__":
    test_udvozles("Felhasználó")
    print("Minden teszt sikeresen lefutott.")
