import os
import shutil
import csv

with open('C:\\dump\\test\\51_042_050.csv','r') as foo:
    foocsv = csv.reader(foo,delimiter = ',',dialect='excel')
    print ' starting'
    for line in foocsv:
        if 'NOM' in line:
            continue
        bdfd = r"\\fs-ld\Losange-Deploiement\Direction Ingenierie\Public\SIG\BD_REFERENCE\CADASTRE\RASTER\BdParcRasterLosange\51\1_DONNEES_LIVRAISON_2017-06-00186\BDPI_1-2_TIF_LAMB93_D051"
        for bar in os.listdir(bdfd):           
            if str(line[0]) == bar[:-4]:
                print line[0], bar[:-4],str(line[0]) == bar[:-4]
                shutil.copyfile(bdfd + '\\' + bar, 'c:\\dump\\test\\' + bar)
                print 'done'