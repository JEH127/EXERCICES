def tri_croissant(x):
    n = len(x)
    # 2 index dans liste x
    for i in range(n):
        for j in range(n):
            # compare valeurs de x[i] et x[j]
            if x[i] >= x[j] and i <= j:
                # permutation et ordre croissant
                x[i], x[j] = x[j], x[i]
    return x


liste_1 = [1, 7, 3]
print(tri_croissant(liste_1))
