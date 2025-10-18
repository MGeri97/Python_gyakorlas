# Python Practicing

[](https://github.com/MGeri97/Python_gyakorlas/actions/workflows/python-app.yml)![Python CI](https://github.com/MGeri97/Python_gyakorlas/actions/workflows/python-app.yml/badge.svg)[](https://github.com/MGeri97/Python_gyakorlas/actions/workflows/code-quality.yml)![Code Quality](https://github.com/MGeri97/Python_gyakorlas/actions/workflows/code-quality.yml/badge.svg)

## Description

Simple Python calculator program with various mathematical operations and an interactive menu.

## Functions

- ➕ **Addition** - Add two numbers
- ➖ **Subtraction** - Subtract two numbers
- ✖️ **Multiplication** - Multiplying two numbers
- ➗ **Division** - Divide two numbers (handle division by zero)
- 🔢 **Exponentiation** - Calculating the power of a number
- 🔵 **Circle Area** - Calculate the area of ​​a circle based on its radius
- 🖥️ **Interactive Menu** - User-friendly choices

## Use

### Interactive mode

```bash
python szamologep.py
```

### Use in a program

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

### Error handling

```python
from szamologep import osztas

try:
    eredmeny = osztas(10, 0)
except ZeroDivisionError as e:
    print(f"Hiba: {e}")  # Nullával való osztás nem lehetséges.
```

## Features

### ✨ **User-friendly interface**

- Simple menu system
- Clear instructions
- Error handling and feedback

### 🛡️ **Error handling**

- Division by zero protection
- Handling invalid input
- Detailed error messages

### 🧮 **Mathematical precision**

- Float type calculations
- Using the PI constant for circle area
- Precise results

## Development

### Prerequisites

```bash
python >= 3.8
```

### Installation

```bash
git clone https://github.com/MGeri97/Python_gyakorlas.git
cd Python_gyakorlas
pip install -r requirements.txt
```

### Testing

```bash
# Összes teszt futtatása
pytest

# Verbose mód
pytest -v

# Csak egy teszt fájl
pytest test_szamologep.py
```

### Code quality control

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

### Automatic formatting

```bash
# Kód formázása
black .

# Import rendezés
isort .
```

## GitHub Actions

The project has an automatic CI/CD pipeline:

### 🔧 **Python CI Workflow**

- Run: Commit in message for `[test]` or `[ci]`
- Python versions: 3.8, 3.9, 3.10, 3.11, 3.12
- Running tests with `pytest`
- Code quality control with `flake8`

### 🎨 **Code Quality Workflow**

- Run: Commit message for `[quality]` or `[ci]`
- Code formatting check ( `black` )
- Import sort check ( `isort` )
- Type checking ( `mypy` )
- Detailed code quality ( `pylint` )

### 📝 **Commit messages**

```bash
# Run tests only
git commit -m "Fix calculator bug [test]"

# Run code quality check only
git commit -m "Update documentation [quality]"

# Run both
git commit -m "Major refactor [ci]"

# No tests are performed
git commit -m "Update README"
```

## File structure

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

## Contribution

1. Fork the repository
2. Create a feature branch ( `git checkout -b feature/new-feature` )
3. Commit the changes ( `git commit -am 'Add new feature [test]'` )
4. Push-release the branch ( `git push origin feature/new-feature` )
5. Create a Pull Request

## License

This project is for educational purposes.

## Contact

**Author:** MGeri97
 **Repository:** https://github.com/MGeri97/Python_practice
