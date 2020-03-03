numbers = [1, 1, 2, 3, 4]
first = set(numbers)
second = {1, 5}
print(first)
print(first | second)  # = > union des 2 sets sans doublon
print(first & second)  # = > point commun des 2 sets
print(first - second)  # = > différences entre les 2 sets
# = > différence symétrique entre les 2 sets ( enlève les points communs )
print(first ^ second)

if 1 in first:
    print("yes")
