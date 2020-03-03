liste_notes = [56, 90, 86, 84, 83, 93, 79]
liste_a_plus = []
liste_a_moins = []

for la_note in liste_notes:
    if la_note > 85:
        liste_a_plus.append(la_note)

    else:
        liste_a_moins.append(la_note)

print(liste_a_plus)
print(liste_a_moins)
