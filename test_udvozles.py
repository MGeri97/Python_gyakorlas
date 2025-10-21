"""
Üdvözlő program tesztelése
"""

from unittest.mock import patch
from io import StringIO
from udvozles import udvozles


def test_udvozles():
    """Teszt az üdvözlő funkcióhoz - mock input és ellenőrizzük a kimenetet"""
    # Mock az input függvényt, hogy "Teszt Felhasználó"-t adja vissza
    with patch("builtins.input", return_value="Teszt Felhasználó"):
        # Elfogni a print kimenetet
        captured_output = StringIO()
        with patch("sys.stdout", captured_output):
            udvozles()

        # Ellenőrizni, hogy a várt üzenet jelent meg
        output = captured_output.getvalue().strip()
        assert output == "Üdvözlöm, Teszt Felhasználó!"


def test_udvozles_empty_name():
    """Teszt üres névvel"""
    with patch("builtins.input", return_value=""):
        captured_output = StringIO()
        with patch("sys.stdout", captured_output):
            udvozles()

        output = captured_output.getvalue().strip()
        assert output == "Üdvözlöm, !"


if __name__ == "__main__":
    test_udvozles()
    test_udvozles_empty_name()
    print("Minden teszt sikeresen lefutott!")
