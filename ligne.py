with open(r"C:\Users\\jamalh\Desktop\test_line.txt", 'w') as f:
    file_w = f.write("AAA.\nBBB.\nCCC.\nDDD.\nEEE.")

with open(r"C:\Users\jamalh\Desktop\test_line.txt", 'r') as f:
 ### ligne par ligne ###
    for ligne in f.readlines():
        print(ligne)
