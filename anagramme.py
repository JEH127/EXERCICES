liste_word = []
word = input("Enter a word : ")

for i in word:
    liste_word.append(i)

if liste_word == liste_word[::-1]:
    print(f"{liste_word} : anagramme")

else:
    print(f"{liste_word} : pas anagramme")
