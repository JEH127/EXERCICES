import time

# => Tue Sep 17 15:26:02 2019
print(time.asctime())
print(time.gmtime())


def duree(x):
    start_time = time.time()
    for i in range(x):
        print(i)

    end_time = time.time()
    time_lapse = end_time - start_time
    print(f"Temps passé : {time_lapse} s")


duree(1001)
