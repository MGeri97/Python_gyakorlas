# Python Gyakorlás

[![Python CI](https://github.com/MGeri97/Python_gyakorlas/actions/workflows/python-app.yml/badge.svg)](https://github.com/MGeri97/Python_gyakorlas/actions/workflows/python-app.yml)
[![Code Quality](https://github.com/MGeri97/Python_gyakorlas/actions/workflows/code-quality.yml/badge.svg)](https://github.com/MGeri97/Python_gyakorlas/actions/workflows/code-quality.yml)

## Leírás

Egyszerű Python számológép program különböző matematikai műveletekkel és interaktív menüvel.

## Funkciók

- ➕ **Összeadás** - Két szám összeadása
- ➖ **Kivonás** - Két szám kivonása  
- ✖️ **Szorzás** - Két szám szorzása
- ➗ **Osztás** - Két szám osztása (nullával való osztás kezelése)
- 🔢 **Hatványozás** - Egy szám hatványának kiszámítása
- 🔵 **Kör területe** - Kör területének kiszámítása sugár alapján
- 🖥️ **Interaktív menü** - Felhasználóbarát választási lehetőségek

## Használat

### Interaktív mód
```bash
python szamologep.py
```

### Programban való használat
```python
from szamologep import osszeadas, kivonas, szorzas, osztas, hatvanyozas, kor_terulet

# Alapvető műveletek
print(osszeadas(5, 3))      # 8
print(kivonas(10, 4))       # 6
print(szorzas(3, 7))        # 21
print(osztas(15, 3))        # 5.0

# Haladó műveletek
print(hatvanyozas(2, 8))    # 256
print(kor_terulet(5))       # 78.53981633974483 (π × r²)
```

### Hiba kezelés
```python
from szamologep import osztas

try:
    eredmeny = osztas(10, 0)
except ZeroDivisionError as e:
    print(f"Hiba: {e}")  # Nullával való osztás nem lehetséges.
```

## Jellemzők

### ✨ **Felhasználóbarát interfész**
- Egyszerű menü rendszer
- Világos utasítások
- Hiba kezelés és visszajelzés

### 🛡️ **Hibakezelés**
- Nullával való osztás védelme
- Érvénytelen input kezelése
- Részletes hibaüzenetek

### 🧮 **Matematikai pontosság**
- Float típusú számítások
- PI konstans használata kör területnél
- Precíz eredmények

## Fejlesztés

### Előfeltételek
```bash
python >= 3.8
```

### Telepítés
```bash
git clone https://github.com/MGeri97/Python_gyakorlas.git
cd Python_gyakorlas
pip install -r requirements.txt
```

### Tesztelés
```bash
# Összes teszt futtatása
pytest

# Verbose mód
pytest -v

# Csak egy teszt fájl
pytest test_szamologep.py
```

### Kód minőség ellenőrzés
```bash
# Formázás ellenőrzés
black --check .

# Import rendezés
isort --check-only .

# Linting
flake8 .

# Típus ellenőrzés
mypy szamologep.py
```

### Automatikus formázás
```bash
# Kód formázása
black .

# Import rendezés
isort .
```

## GitHub Actions

A projekt automatikus CI/CD pipeline-nal rendelkezik:

### 🔧 **Python CI Workflow**
- Futtatás: Commit üzenetben `[test]` vagy `[ci]` esetén
- Python verziók: 3.8, 3.9, 3.10, 3.11, 3.12
- Tesztek futtatása `pytest`-tel
- Kód minőség ellenőrzés `flake8`-cal

### 🎨 **Code Quality Workflow**  
- Futtatás: Commit üzenetben `[quality]` vagy `[ci]` esetén
- Kód formázás ellenőrzés (`black`)
- Import rendezés ellenőrzés (`isort`)
- Típus ellenőrzés (`mypy`)
- Részletes kód minőség (`pylint`)

### 📝 **Commit üzenetek**
```bash
# Csak tesztek futtatása
git commit -m "Fix calculator bug [test]"

# Csak kód minőség ellenőrzés
git commit -m "Update documentation [quality]"

# Mind a kettő futtatása
git commit -m "Major refactor [ci]"

# Semmi sem fut
git commit -m "Update README"
```

## Fájl struktúra

```
Python_gyakorlas/
├── szamologep.py           # Fő számológép modul
├── test_szamologep.py      # Unit tesztek
├── requirements.txt        # Python függőségek
├── README.md              # Dokumentáció
└── .github/
    └── workflows/
        ├── python-app.yml      # CI pipeline
        └── code-quality.yml    # Kód minőség ellenőrzés
```

## Hozzájárulás

1. Fork-old a repository-t
2. Hozz létre egy feature branch-et (`git checkout -b feature/new-feature`)
3. Commit-old a változtatásokat (`git commit -am 'Add new feature [test]'`)
4. Push-old a branch-et (`git push origin feature/new-feature`)
5. Hozz létre egy Pull Request-et

## Licenc

Ez a projekt oktatási célokat szolgál.

## Kapcsolat

**Szerző:** MGeri97  
**Repository:** https://github.com/MGeri97/Python_gyakorlas