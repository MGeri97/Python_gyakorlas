# Importok végrehajtása
import math
import os
from datetime import datetime
from typing import List, Tuple

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

PI = math.pi
console = Console()


# Alapvető matematikai műveletek
def osszeadas(a, b):
    """Két szám összeadása"""
    return a + b


def kivonas(a, b):
    """Két szám kivonása"""
    return a - b


def szorzas(a, b):
    """Két szám szorzása"""
    return a * b


def osztas(a, b):
    """Két szám osztása"""
    if b == 0:
        raise ZeroDivisionError("Nullával való osztás nem lehetséges.")
    return a / b


def hatvanyozas(a, b):
    """Két szám hatványozása"""
    return a**b


def kor_terulet(r):
    """Kör területének kiszámítása"""
    return PI * r * r


def kor_kerulet(r):
    """Kör kerületének kiszámítása"""
    return 2 * r * PI


# Új haladó matematikai műveletek
def gyok(a):
    """Négyzetgyök kiszámítása"""
    if a < 0:
        raise ValueError("Negatív szám gyökét nem lehet kiszámítani.")
    return math.sqrt(a)


def sin(a):
    """Szinusz kiszámítása (radiánban)"""
    return math.sin(a)


def cos(a):
    """Koszinusz kiszámítása (radiánban)"""
    return math.cos(a)


def tan(a):
    """Tangens kiszámítása (radiánban)"""
    return math.tan(a)


def log(a):
    """Természetes logaritmus kiszámítása"""
    if a <= 0:
        raise ValueError("Logaritmus csak pozitív számokra értelmezhető.")
    return math.log(a)


def log10(a):
    """10-es alapú logaritmus kiszámítása"""
    if a <= 0:
        raise ValueError("Logaritmus csak pozitív számokra értelmezhető.")
    return math.log10(a)


# Memória és előzmény kezelés
class CalculatorMemory:
    """Számológép memória és előzmények kezelése"""

    def __init__(self):
        self.memory = 0.0
        self.history: List[Tuple[str, float, str]] = []

    def memory_add(self, value: float):
        """Érték hozzáadása a memóriához (M+)"""
        self.memory += value

    def memory_subtract(self, value: float):
        """Érték kivonása a memóriából (M-)"""
        self.memory -= value

    def memory_recall(self) -> float:
        """Memória visszahívása (MR)"""
        return self.memory

    def memory_clear(self):
        """Memória törlése (MC)"""
        self.memory = 0.0

    def add_history(self, operation: str, result: float, timestamp: str = None):
        """Művelet hozzáadása az előzményekhez"""
        if timestamp is None:
            timestamp = datetime.now().strftime("%H:%M:%S")
        self.history.append((operation, result, timestamp))

    def get_history(self) -> List[Tuple[str, float, str]]:
        """Előzmények lekérése"""
        return self.history

    def clear_history(self):
        """Előzmények törlése"""
        self.history = []


# Globális memória példány
calc_memory = CalculatorMemory()


# Képernyő törlése
def clear_screen():
    """Képernyő törlése"""
    os.system("clear" if os.name != "nt" else "cls")


# Szám bekérése validálással
def beolvas_szam(prompt: str) -> float:
    """Egy szám bekérése validálással"""
    while True:
        try:
            value = input(prompt)
            return float(value)
        except ValueError:
            console.print("[bold red]Hibás bemenet! Kérlek számot adj meg.[/bold red]")


# Két szám bekérése
def beolvas_szamok():
    a = beolvas_szam("Kérem az első számot (pontot használj tizedesjegyként!): ")
    b = beolvas_szam("Kérem a második számot (pontot használj tizedesjegyként!): ")
    return a, b


# TUI megjelenítés
def megjelenit_fejlec():
    """Fejléc megjelenítése rich stílussal"""
    fejlec = Panel(
        Text("🧮 TOVÁBBFEJLESZTETT SZÁMOLÓGÉP 🧮", justify="center", style="bold cyan"),
        style="bold blue",
    )
    console.print(fejlec)


def megjelenit_menu():
    """Menü megjelenítése táblázatban"""
    table = Table(
        title="📋 Műveletek Menü", show_header=True, header_style="bold magenta"
    )
    table.add_column("Szám", style="cyan", width=6)
    table.add_column("Művelet", style="green")
    table.add_column("Szám", style="cyan", width=6)
    table.add_column("Művelet", style="green")

    table.add_row("1", "➕ Összeadás", "11", "📐 Szinusz")
    table.add_row("2", "➖ Kivonás", "12", "📐 Koszinusz")
    table.add_row("3", "✖️ Szorzás", "13", "📐 Tangens")
    table.add_row("4", "➗ Osztás", "14", "📊 Logaritmus (ln)")
    table.add_row("5", "🔢 Hatványozás", "15", "📊 Logaritmus (log10)")
    table.add_row("6", "🔵 Kör területe", "M+", "💾 Memóriába ad")
    table.add_row("7", "⭕ Kör kerülete", "M-", "💾 Memóriából kivon")
    table.add_row("8", "√ Négyzetgyök", "MR", "💾 Memória visszahívás")
    table.add_row("9", "📜 Előzmények", "MC", "💾 Memória törlés")
    table.add_row("10", "🗑️ Előzmények törlése", "H", "❓ Súgó")
    table.add_row("0", "❌ Kilépés", "", "")

    console.print(table)


def megjelenit_elozmenyeket():
    """Előzmények megjelenítése"""
    history = calc_memory.get_history()
    if not history:
        console.print("[yellow]Nincs még művelet az előzményekben.[/yellow]")
        return

    table = Table(
        title="📜 Számítási Előzmények", show_header=True, header_style="bold cyan"
    )
    table.add_column("Idő", style="dim", width=10)
    table.add_column("Művelet", style="white")
    table.add_column("Eredmény", style="green", justify="right")

    for op, result, time in history[-10:]:  # Csak az utolsó 10
        table.add_row(time, op, f"{result:.6g}")

    console.print(table)


def megjelenit_memoria():
    """Memória állapot megjelenítése"""
    mem_value = calc_memory.memory_recall()
    if mem_value != 0:
        console.print(f"[bold yellow]💾 Memória: {mem_value:.6g}[/bold yellow]")


def megjelenit_sugo():
    """Súgó megjelenítése"""
    sugo_text = """
[bold cyan]Használati útmutató:[/bold cyan]

[bold green]Alapműveletek:[/bold green]
  • 1-7: Két szám közötti műveletek
  • 8: Négyzetgyök (egy szám)
  • 11-15: Trigonometrikus és logaritmikus műveletek (egy szám)

[bold green]Memória műveletek:[/bold green]
  • M+: Utolsó eredmény hozzáadása a memóriához
  • M-: Utolsó eredmény kivonása a memóriából
  • MR: Memória értékének megjelenítése
  • MC: Memória törlése

[bold green]Egyéb funkciók:[/bold green]
  • 9: Előzmények megtekintése
  • 10: Előzmények törlése
  • H: Ez a súgó
  • 0: Kilépés a programból

[bold yellow]Tippek:[/bold yellow]
  • Trigonometrikus függvények radiánban dolgoznak
  • Az eredmények automatikusan az előzményekbe kerülnek
  • A memória funkciók az utolsó eredménnyel dolgoznak
    """
    panel = Panel(sugo_text, title="❓ Súgó", border_style="blue")
    console.print(panel)


def utasitasok():
    """Utasítások megjelenítése (régi kompatibilitás)"""
    megjelenit_menu()


def main():
    """Főprogram továbbfejlesztett TUI-vel"""
    utolso_eredmeny = None

    while True:
        clear_screen()
        megjelenit_fejlec()
        megjelenit_memoria()
        megjelenit_menu()

        valasztas = input("\n🔢 Válassz műveletet: ").strip().upper()

        if valasztas == "0":
            console.print(
                "[bold green]👋 Viszlát! Köszönöm a használatot![/bold green]"
            )
            break

        elif valasztas == "9":
            clear_screen()
            megjelenit_fejlec()
            megjelenit_elozmenyeket()
            input("\n⏎ Nyomj Enter-t a folytatáshoz...")
            continue

        elif valasztas == "10":
            calc_memory.clear_history()
            console.print("[bold green]✓ Előzmények törölve![/bold green]")
            input("\n⏎ Nyomj Enter-t a folytatáshoz...")
            continue

        elif valasztas == "H":
            clear_screen()
            megjelenit_fejlec()
            megjelenit_sugo()
            input("\n⏎ Nyomj Enter-t a folytatáshoz...")
            continue

        elif valasztas == "M+":
            if utolso_eredmeny is not None:
                calc_memory.memory_add(utolso_eredmeny)
                uj_ertek = calc_memory.memory_recall()
                console.print(
                    f"[bold green]✓ {utolso_eredmeny:.6g} hozzáadva a memóriához! "
                    f"Új érték: {uj_ertek:.6g}[/bold green]"
                )
            else:
                console.print(
                    "[bold red]Nincs még eredmény a memóriához adáshoz![/bold red]"
                )
            input("\n⏎ Nyomj Enter-t a folytatáshoz...")
            continue

        elif valasztas == "M-":
            if utolso_eredmeny is not None:
                calc_memory.memory_subtract(utolso_eredmeny)
                uj_ertek = calc_memory.memory_recall()
                console.print(
                    f"[bold green]✓ {utolso_eredmeny:.6g} kivonva a memóriából! "
                    f"Új érték: {uj_ertek:.6g}[/bold green]"
                )
            else:
                console.print(
                    "[bold red]Nincs még eredmény a memóriából kivonáshoz![/bold red]"
                )
            input("\n⏎ Nyomj Enter-t a folytatáshoz...")
            continue

        elif valasztas == "MR":
            mem_val = calc_memory.memory_recall()
            console.print(
                f"[bold yellow]💾 Memória értéke: {mem_val:.6g}[/bold yellow]"
            )
            input("\n⏎ Nyomj Enter-t a folytatáshoz...")
            continue

        elif valasztas == "MC":
            calc_memory.memory_clear()
            console.print("[bold green]✓ Memória törölve![/bold green]")
            input("\n⏎ Nyomj Enter-t a folytatáshoz...")
            continue

        # Műveletek végrehajtása
        try:
            if valasztas in ["1", "2", "3", "4", "5"]:
                console.print("\n[cyan]Két szám bekérése:[/cyan]")
                a, b = beolvas_szamok()

                if valasztas == "1":
                    eredmeny = osszeadas(a, b)
                    muvelet = f"{a:.6g} + {b:.6g}"
                elif valasztas == "2":
                    eredmeny = kivonas(a, b)
                    muvelet = f"{a:.6g} - {b:.6g}"
                elif valasztas == "3":
                    eredmeny = szorzas(a, b)
                    muvelet = f"{a:.6g} × {b:.6g}"
                elif valasztas == "4":
                    eredmeny = osztas(a, b)
                    muvelet = f"{a:.6g} ÷ {b:.6g}"
                elif valasztas == "5":
                    eredmeny = hatvanyozas(a, b)
                    muvelet = f"{a:.6g} ^ {b:.6g}"

            elif valasztas in ["6", "7", "8", "11", "12", "13", "14", "15"]:
                console.print("\n[cyan]Egy szám bekérése:[/cyan]")
                a = beolvas_szam("Kérem a számot: ")

                if valasztas == "6":
                    eredmeny = kor_terulet(a)
                    muvelet = f"Kör területe (r={a:.6g})"
                elif valasztas == "7":
                    eredmeny = kor_kerulet(a)
                    muvelet = f"Kör kerülete (r={a:.6g})"
                elif valasztas == "8":
                    eredmeny = gyok(a)
                    muvelet = f"√{a:.6g}"
                elif valasztas == "11":
                    eredmeny = sin(a)
                    muvelet = f"sin({a:.6g})"
                elif valasztas == "12":
                    eredmeny = cos(a)
                    muvelet = f"cos({a:.6g})"
                elif valasztas == "13":
                    eredmeny = tan(a)
                    muvelet = f"tan({a:.6g})"
                elif valasztas == "14":
                    eredmeny = log(a)
                    muvelet = f"ln({a:.6g})"
                elif valasztas == "15":
                    eredmeny = log10(a)
                    muvelet = f"log10({a:.6g})"

            else:
                console.print("[bold red]❌ Érvénytelen választás![/bold red]")
                input("\n⏎ Nyomj Enter-t a folytatáshoz...")
                continue

            # Eredmény megjelenítése
            utolso_eredmeny = eredmeny
            calc_memory.add_history(muvelet, eredmeny)

            eredmeny_panel = Panel(
                f"[bold green]{muvelet} = {eredmeny:.10g}[/bold green]",
                title="✨ Eredmény",
                border_style="green",
            )
            console.print("\n")
            console.print(eredmeny_panel)

        except (ZeroDivisionError, ValueError) as e:
            console.print(f"[bold red]❌ Hiba: {e}[/bold red]")

        except Exception as e:
            console.print(f"[bold red]❌ Váratlan hiba: {e}[/bold red]")

        input("\n⏎ Nyomj Enter-t a folytatáshoz...")


if __name__ == "__main__":
    main()
