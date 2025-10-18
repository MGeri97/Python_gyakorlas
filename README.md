# Python Gyakorlás

[![Python CI](https://github.com/MGeri97/Python_gyakorlas/actions/workflows/python-app.yml/badge.svg)](https://github.com/MGeri97/Python_gyakorlas/actions/workflows/python-app.yml)
[![Code Quality](https://github.com/MGeri97/Python_gyakorlas/actions/workflows/code-quality.yml/badge.svg)](https://github.com/MGeri97/Python_gyakorlas/actions/workflows/code-quality.yml)

## Leírás

Egyszerű Python számológép program különböző matematikai műveletekkel.

## Funkciók

- Összeadás
- Kivonás  
- Szorzás
- Osztás

## Használat

```python
from szamologep import osszeadas, kivonas, szorzas, osztas

# Példák
print(osszeadas(5, 3))  # 8
print(kivonas(10, 4))   # 6
print(szorzas(3, 7))    # 21
print(osztas(15, 3))    # 5.0
```

## Fejlesztés

### Telepítés
```bash
pip install -r requirements.txt
```

### Tesztelés
```bash
pytest
```

### Kód formázás
```bash
black .
isort .
```