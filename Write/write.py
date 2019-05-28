import csv

def write_ar(archivo,nombre=str):
    myFile=open(nombre, 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(archivo)

    print("Writing complete")
