import random

polozky = ["kabát", "chleba", "bicykl", "sýr", "automobil"]

for _ in range(10):
    osoba1 = random.choice(polozky)
    osoba2 = random.choice(polozky)

    print(f"- Kupme {osoba1}.")

    if osoba1 == osoba2:

        moznosti = [p for p in polozky if p != osoba1]
        jina_polozka = random.choice(moznosti)
        print(f"- Ne, kupme jiný {jina_polozka}.")
    else:
     
        print(f"- Ne, kupme {osoba2}.")
