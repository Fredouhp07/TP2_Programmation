import csv


def charger_pokemons_csv(fichier):
    dct = {}
    with open(fichier, encoding="utf-8") as fvsc:  # fichier csv
        fr = csv.reader(fvsc)  # fichier read
        for row in fr:
            dct[row[0]] = []
            for stat in row[1:]:
                dct[row[0]].append(int(stat))
            # print(dct)
            pass
        fvsc.close()
    return dct


# print(charger_pokemons_csv("pokemon.csv"))

pkmn = charger_pokemons_csv("pokemon.csv")
for nom, stats in pkmn.items():
    print(f"{nom}: {stats}")

pkmn = charger_pokemons_csv("pokemon.csv")
print(isinstance(pkmn, dict))
print(isinstance(pkmn["Pikachu"], list))
print(isinstance(pkmn["Pikachu"][0], int))
