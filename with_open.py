def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")


def get_greeting(name):
    return f"Hi {name}"


chemin = r"C:\Users\jamalh\Desktop\content.txt"
message = get_greeting("Mosh")

with open(chemin, 'w') as f:  # r ou \\ => car \
    file_w = f.write(message)

with open(chemin, 'r') as f:
    file_r = f.read()
    print(file_r)

# file = open(chemin, 'w')
# file.write(message)
