var = 'o'

while var == 'o':
    x = int(input(' Entrez un nombre entier : '))

    table = [i for i in range(x)]
    print(table)

    var = input(' Voulez-vous continuer : o / n ?\n ')
    if var == 'o':
        # continue => revient au début de la boucle while ou for
        continue
    else:
        # sortie de la boucle
        break

print(' Au revoir ')
