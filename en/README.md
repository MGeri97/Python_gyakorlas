# Python Practicing

[](https://github.com/MGeri97/Python_gyakorlas/actions/workflows/python-app.yml)![Python CI](https://github.com/MGeri97/Python_gyakorlas/actions/workflows/python-app.yml/badge.svg)[](https://github.com/MGeri97/Python_gyakorlas/actions/workflows/code-quality.yml)![Code Quality](https://github.com/MGeri97/Python_gyakorlas/actions/workflows/code-quality.yml/badge.svg)

## Description

Advanced Python calculator program with modern TUI (Text User Interface), various mathematical operations, and an interactive menu.

## Functions

### 🎨 Modern TUI Interface
- 🖥️ **Rich library** - Colorful, formatted terminal interface
- 📋 **Tabular menu** - Easy-to-navigate operations
- 🎯 **Panel display** - Elegant result formatting
- ❓ **Built-in help** - Detailed usage guide

### ➕ Basic Operations
- ➕ **Addition** - Add two numbers
- ➖ **Subtraction** - Subtract two numbers
- ✖️ **Multiplication** - Multiply two numbers
- ➗ **Division** - Divide two numbers (handle division by zero)
- 🔢 **Exponentiation** - Calculate power of a number

### 🔬 Advanced Operations
- √ **Square Root** - Calculate square root
- 📐 **Sine** - Sine function (in radians)
- 📐 **Cosine** - Cosine function (in radians)
- 📐 **Tangent** - Tangent function (in radians)
- 📊 **Natural Logarithm** - Calculate ln(x)
- 📊 **Base-10 Logarithm** - Calculate log10(x)
- 🔵 **Circle Area** - Calculate circle area from radius
- ⭕ **Circle Circumference** - Calculate circle circumference from radius

### 💾 Memory Functions
- **M+** - Add value to memory
- **M-** - Subtract value from memory
- **MR** - Recall memory contents
- **MC** - Clear memory

### 📜 History
- **Automatic tracking** - All operations are saved
- **Timestamps** - Time-stamped calculations
- **View** - Display last 10 operations
- **Clear** - Clear history

## Use

### Interactive mode

```bash
python szamologep.py
```

### Use in a program

```python
from szamologep import (
    osszeadas, kivonas, szorzas, osztas, hatvanyozas,
    kor_terulet, kor_kerulet, gyok, sin, cos, tan, log, log10,
    CalculatorMemory
)

# Basic operations
print(osszeadas(5, 3))      # 8
print(kivonas(10, 4))       # 6
print(szorzas(3, 7))        # 21
print(osztas(15, 3))        # 5.0

# Advanced operations
print(hatvanyozas(2, 8))    # 256
print(gyok(16))             # 4.0
print(sin(0))               # 0.0
print(cos(0))               # 1.0
print(log(2.718281828))     # ~1.0
print(log10(100))           # 2.0
print(kor_terulet(5))       # 78.53981633974483 (π × r²)
print(kor_kerulet(5))       # 31.41592653589793 (2 × π × r)

# Memory usage
memory = CalculatorMemory()
memory.memory_add(10)
memory.memory_add(5)
print(memory.memory_recall())  # 15.0
memory.memory_clear()
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
