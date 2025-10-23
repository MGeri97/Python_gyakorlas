# Python Gyakorlás

[![Python CI](https://github.com/MGeri97/Python_gyakorlas/actions/workflows/python-app.yml/badge.svg)](https://github.com/MGeri97/Python_gyakorlas/actions/workflows/python-app.yml)
[![Code Quality](https://github.com/MGeri97/Python_gyakorlas/actions/workflows/code-quality.yml/badge.svg)](https://github.com/MGeri97/Python_gyakorlas/actions/workflows/code-quality.yml)

## Leírás

Továbbfejlesztett Python számológép program modern TUI (Text User Interface) felülettel, különböző matematikai műveletekkel és interaktív menüvel.
Üdvözlő program is található benne (`udvozles.py`), amely bekéri a felhasználó nevét és üdvözli őt.

## Funkciók

### Számológép (`szamologep.py`)

#### 🎨 Modern TUI Felület
- 🖥️ **Rich könyvtár** - Színes, formázott terminál felület
- 📋 **Táblázatos menü** - Könnyen áttekinthető műveletek
- 🎯 **Paneles megjelenítés** - Elegáns eredmény formázás
- ❓ **Beépített súgó** - Részletes használati útmutató

#### ➕ Alapműveletek
- ➕ **Összeadás** - Két szám összeadása
- ➖ **Kivonás** - Két szám kivonása  
- ✖️ **Szorzás** - Két szám szorzása
- ➗ **Osztás** - Két szám osztása (nullával való osztás kezelése)
- 🔢 **Hatványozás** - Egy szám hatványának kiszámítása

#### 🔬 Haladó műveletek
- √ **Négyzetgyök** - Négyzetgyök kiszámítása
- 📐 **Szinusz** - Szinusz függvény (radiánban)
- 📐 **Koszinusz** - Koszinusz függvény (radiánban)
- 📐 **Tangens** - Tangens függvény (radiánban)
- 📊 **Természetes logaritmus** - ln(x) kiszámítása
- 📊 **10-es alapú logaritmus** - log10(x) kiszámítása
- 🔵 **Kör területe** - Kör területének kiszámítása sugár alapján
- ⭕ **Kör kerülete** - Kör kerületének kiszámítása sugár alapján

#### 💾 Memória funkciók
- **M+** - Érték hozzáadása a memóriához
- **M-** - Érték kivonása a memóriából
- **MR** - Memória tartalmának visszahívása
- **MC** - Memória törlése

#### 📜 Előzmények
- **Automatikus nyilvántartás** - Minden művelet mentésre kerül
- **Időbélyegzés** - Pontos idővel ellátott előzmények
- **Megtekintés** - Utolsó 10 művelet megjelenítése
- **Törlés** - Előzmények törlése

### Üdvözlő program (`udvozles.py`)
- 👋 **Személyes üdvözlés** - Bekéri és üdvözli a felhasználót

## Használat

### Interaktív mód
```bash
# Számológép program
python szamologep.py

# Üdvözlő program
python udvozles.py
```

### Programban való használat
```python
from szamologep import (
    osszeadas, kivonas, szorzas, osztas, hatvanyozas, 
    kor_terulet, kor_kerulet, gyok, sin, cos, tan, log, log10,
    CalculatorMemory
)

# Alapvető műveletek
print(osszeadas(5, 3))      # 8
print(kivonas(10, 4))       # 6
print(szorzas(3, 7))        # 21
print(osztas(15, 3))        # 5.0

# Haladó műveletek
print(hatvanyozas(2, 8))    # 256
print(gyok(16))             # 4.0
print(sin(0))               # 0.0
print(cos(0))               # 1.0
print(log(2.718281828))     # ~1.0
print(log10(100))           # 2.0
print(kor_terulet(5))       # 78.53981633974483 (π × r²)
print(kor_kerulet(5))       # 31.41592653589793 (2 × π × r)

# Memória használata
memory = CalculatorMemory()
memory.memory_add(10)
memory.memory_add(5)
print(memory.memory_recall())  # 15.0
memory.memory_clear()
```

### Üdvözlő program használata
```bash
python udvozles.py
```

```python
from udvozles import udvozles

udvozles()  # Interaktív név bekérés és üdvözlés
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

### ✨ **Felhasználóbarát TUI interfész**
- Modern, színes terminál megjelenés (`rich` könyvtár)
- Táblázatos menü rendszer könnyű navigációval
- Világos utasítások és visszajelzések
- Paneles eredmény megjelenítés
- Képernyő törlés és átlátható felület

### 🛡️ **Hibakezelés**
- Nullával való osztás védelme
- Negatív gyök védelem
- Negatív/nulla logaritmus védelem
- Érvénytelen input kezelése
- Részletes hibaüzenetek

### 🧮 **Matematikai pontosság**
- Float típusú számítások
- Math könyvtár használata pontos trigonometrikus és logaritmikus függvényekhez
- PI konstans használata kör területnél és kerületnél
- Precíz eredmények

### 💾 **Memória és előzmények**
- Memória műveletek (M+, M-, MR, MC)
- Automatikus előzmény rögzítés
- Időbélyegzett számítások
- Legutóbbi 10 művelet megtekintése

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

A függőségek tartalmazzák:
- `pytest` - Teszteléshez
- `rich` - Modern TUI felülethez
- `black`, `isort`, `flake8`, `pylint`, `mypy` - Kód minőség ellenőrzéshez

### Tesztelés
```bash
# Összes teszt futtatása
pytest

# Verbose mód
pytest -v

# Csak egy teszt fájl
pytest test_szamologep.py

VAGY

pytest test_udvozles.py
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
├── udvozles.py            # Üdvözlő program
├── test_szamologep.py      # Unit tesztek a számológéphez
├── test_udvozles.py       # Unit tesztek az üdvözlő programhoz
├── requirements.txt        # Python függőségek
├── README.md              # Dokumentáció
├── en/                    # Angol dokumentáció
│   └── README.md
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