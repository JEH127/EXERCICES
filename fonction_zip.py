list1 = [1, 2, 3, 4, 5]
list2 = ['one', 'two', 'three', 'four', 'five']

zipped = list(zip(list1, list2))
# => [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')]
print(zipped)

unzipped = list(zip(*zipped))
# => [(1, 2, 3, 4, 5), ('one', 'two', 'three', 'four', 'five')]
print(unzipped)
print("*"*50)

for l1, l2 in zip(list1, list2):
    print(l1)
    print(l2)
"""
=>
1
one
2
two
3
three
4
four
5
five
"""
print("*"*50)

list3 = [1, 2, 3]
list4 = [4, 5, 6]

somme_listes = [x + y for x, y in zip(list3, list4)]
print(somme_listes)


sentences = []
items = ['Apple', 'Banana', 'Orange']
counts = [3, 6, 4]
prices = [0.99, 0.25, 0.50]

for (item, count, price) in zip(items, counts, prices):
    sentence = f"I bought {count} {item}s at {price} cents each"
    sentences.append(sentence)
print(sentences)
