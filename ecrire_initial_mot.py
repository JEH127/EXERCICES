def get_initial(name):
    initial = name[0:1]  # ou [0]
    return initial


first_name = input("Quel est votre prénom ? ")
last_name = input("Quel est votre nom ? ")

print(f"Vous êtes : {first_name} {last_name}")
print(
    f"Vos initiales sont : {get_initial(first_name)}{get_initial(last_name)}")
