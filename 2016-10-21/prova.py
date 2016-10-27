from pyplasm import*
import csv
from workshop_01 import*

def floatFromString(stringa):
    lista=[]
    for s in stringa:
        l=float(s)
        lista.append(l)
    return lista
    
def ggpl_bone_structure(file_name):
    with open(file_name,'rb') as csvFile:
        reader = csv.DictReader(csvFile)
        scheletro=QUOTE([0])
        for  row in reader:
            riga=row['telaio']
            lista=riga.split(';')
            
            vettori = floatFromString(lista[0].split(','))
            sezioni = floatFromString(lista[1].split(','))
            distanze = floatFromString(lista[2].split(','))
            altezze = floatFromString(lista[3].split(','))
            
            telaio = fun(sezioni[0],sezioni[1],sezioni[2],sezioni[3],distanze,altezze)
            scheletro = STRUCT([scheletro,T([1,2,3])([vettori[0],vettori[1],vettori[2]])(telaio)])
    return scheletro
    

VIEW(ggpl_bone_structure("frame_data_430379 - Foglio1.csv"))