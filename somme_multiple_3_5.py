somme_multiple_3 = 0
for i in range(1000):
    if i % 3 == 0:
        somme_multiple_3 += i

print(f"somme_multiple_3 < 1000 = {somme_multiple_3}")

somme_multiple_5 = 0
for i in range(1000):
    if i % 5 == 0:
        somme_multiple_5 += i

print(f"somme_multiple_5 < 1000 = {somme_multiple_5}")
