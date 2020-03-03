var = 'o'

while var == 'o':
    x = int(input(' Entrez un nombre entier : '))

    table = [i for i in range(x)]
    print(table)

    var = input(' Voulez-vous continuer : o / n ?\n ')

print(' Au revoir ')
