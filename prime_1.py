def prime(num):
    if num < 2:
        print("Not Prime")
    else:
        # num >= 2
        for i in range(2, num):
            # si num multiple de i => non premier
            if num % i == 0:
                print(f"{num} : Not Prime")
                # si num au moins multiple d'1 seul i => sort de la boucle avec break
                break
        else:
            print(f"{num} : Prime")


prime(100)
