# Importok végrehajtása
import math

PI = math.pi

# Két szám bekérése
def beolvas_szamok():
	a = float(input("Kérem az első számot (pontot használj tizedesjegyként!): "))
	b = float(input("Kérem a második számot (pontot használj tizedesjegyként!): "))
	return a, b

def utasitasok():
	print("Válassz műveletet:")
	print("1 - Összeadás")
	print("2 - Kivonás")
	print("3 - Szorzás")
	print("4 - Osztás")
	print("5 - Kilépés")

def main():
	while True:
		utasitasok()
		valasztas = input("Írd be a választott művelet számát (1/2/3/4/5): ")

		if valasztas == '5':
			print("Kilépés a programból.")
			break

		a, b = beolvas_szamok()

		if valasztas == '1':
			eredmeny = a + b
			muvelet = "összeadás"
		elif valasztas == '2':
			eredmeny = a - b
			muvelet = "kivonás"
		elif valasztas == '3':
			eredmeny = a * b
			muvelet = "szorzás"
		elif valasztas == '4':
			if b != 0:
				eredmeny = a / b
				muvelet = "osztás"
			else:
				print("Hiba: Nullával való osztás nem lehetséges.")
				continue
		else:
			print("Érvénytelen választás. Kérlek próbáld újra.")
			continue

		print(f"A {muvelet} eredménye: {eredmeny}")

if __name__ == "__main__":
	main()