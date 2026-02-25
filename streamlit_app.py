import random

class LabirintDuhovnosti:
    def __init__(self):
        self.razine = ["Ulaz u Tišinu", "Dvorana Refleksije", "Vrt Zahvalnosti", "Središte Mira"]
        self.trenutna_razina = 0
        self.energija = 100

    def opisi_stanje(self):
        print(f"\n--- {self.razine[self.trenutna_razina]} ---")
        print(f"Vaša duhovna energija: {self.energija}%")

    def kreni(self):
        print("Dobrodošli u Labirint Duhovnosti.")
        while self.trenutna_razina < len(self.razine) - 1 and self.energija > 0:
            self.opisi_stanje()
            odluka = input("Želite li ići (naprijed) ili (meditirati)? ").lower()

            if odluka == "naprijed":
                if random.random() > 0.3:
                    print("Uspješno ste prošli dublje u labirint.")
                    self.trenutna_razina += 1
                else:
                    print("Naišli ste na nemirnu misao. Gubite energiju.")
                    self.energija -= 20
            elif odluka == "meditirati":
                print("Meditacijom vraćate mir i energiju.")
                self.energija = min(100, self.energija + 30)
            else:
                print("Nejasna odluka, labirint vas čeka.")

        if self.energija <= 0:
            print("\nIzgubili ste se u mislima. Pokušajte ponovno.")
        else:
            print(f"\nČestitamo! Dosegnuli ste {self.razine[-1]}.")

# Pokretanje aplikacije
if __name__ == "__main__":
    igra = LabirintDuhovnosti()
    igra.kreni()
