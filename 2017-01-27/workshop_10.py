from pyplasm import*
from math import*
import csv

def listFromString(stringa):
    lista=stringa.split(",")
    lista2=[]
    for elem in lista:
        lista2.append(float(elem)/40.)  
    return lista2
    
def designStairs(x,y,z):
    
        
    alzataProvv=0.15
    pedataProvv=0.30
    
    alzata=(z/round(z/alzataProvv))
    pedata=(y/round(y/pedataProvv))
    
   
    numeroScalini=int(z/alzata)
    
    piano = PROD([PROD([QUOTE([0.4]),QUOTE([y])]), QUOTE([z])])
    muro=STRUCT([piano])
   
    scalino= MKPOL([[[0,0,0],[0,0,alzata],[0,pedata,0],[0,pedata*2,alzata],[x,0,0],[x,0,alzata],[x,pedata,0],[x,pedata*2,alzata]],[[1,2,3,4,5,6,7,8]],1])
    
    scala=QUOTE([0])
    altezza=0
    profondita=0
    for i in range(numeroScalini-1):
        scala=STRUCT([scala,T([2,3])([profondita,altezza])(scalino)])
        altezza=altezza+alzata
        profondita=profondita+pedata
    
    ultimoscalino=CUBOID([x,pedata,alzata])
    
    scala=STRUCT([scala,T([2,3])([profondita,altezza])(ultimoscalino)])
    scala=TEXTURE(["PAVIMENTO-TEXTURE-006.jpg",True,False,1,1,0,10,10])(scala)
    muro=TEXTURE(["/Users/caosnumerico/Desktop/Grafica/progetti/development/ggpl/2016-10-28/292453_muro-sfondo-texture-mattone-casa-costruzione.jpg",True,False,1,1,0,5,5])(muro)



    stair=STRUCT([scala])
    return stair
    
def ggpl_svgPorte(file):
    planimetria=QUOTE([0])
    with open(file, 'rb') as csvFile:
        reader = csv.DictReader(csvFile)
        righe=csv.reader(csvFile, delimiter=' ',quotechar='|')
        for riga in righe:
            l=listFromString(riga[0])
            linea=MKPOL([[[l[0],l[1],0],[l[2],l[3],0]],[[1,2]],[1]])
            planimetria=STRUCT([planimetria,linea])
            
    planimetria=OFFSET([0.6,0.6,2.2])(planimetria)
    planimetria=OFFSET([-0.5,-0.2,0])(planimetria)

    
    return planimetria 
    
def ggpl_svgPorte2(file):
    #planimetria=QUOTE([0])
    planimetria = None
    with open(file, 'rb') as csvFile:
        reader = csv.DictReader(csvFile)
        righe=csv.reader(csvFile, delimiter=' ',quotechar='|')
        for riga in righe:
            l=listFromString(riga[0])
            linea=MKPOL([[[l[0],l[1],0],[l[2],l[3],0]],[[1,2]],[1]])
            if planimetria == None:
                planimetria = linea
            else:
                planimetria=STRUCT([planimetria,linea])
        
    planimetria=OFFSET([0.1,0.6,2.2])(planimetria)
    planimetria=OFFSET([-0.1,-0.2,0])(planimetria)
    
    return planimetria 
    
def ggpl_svgFinestre(file):
    #planimetria=QUOTE([0])
    planimetria = None
    with open(file, 'rb') as csvFile:
        reader = csv.DictReader(csvFile)
        righe=csv.reader(csvFile, delimiter=' ',quotechar='|')
        for riga in righe:
            l=listFromString(riga[0])
            linea=MKPOL([[[l[0],l[1],0],[l[2],l[3],0]],[[1,2]],[1]])
            if planimetria == None:
                planimetria = linea
            else:
                planimetria=STRUCT([planimetria,linea])
    
    planimetria=OFFSET([0.4,0.4,1.5])(planimetria)
    planimetria=OFFSET([-0.4,-0.2,0])(planimetria)
    
    return planimetria 
    
def ggpl_svgFinestre2(file):
    #planimetria=QUOTE([0])
    planimetria = None
    with open(file, 'rb') as csvFile:
        reader = csv.DictReader(csvFile)
        righe=csv.reader(csvFile, delimiter=' ',quotechar='|')
        for riga in righe:
            l=listFromString(riga[0])
            linea=MKPOL([[[l[0],l[1],0],[l[2],l[3],0]],[[1,2]],[1]])
            if planimetria == None:
                planimetria = linea
            else:
                planimetria=STRUCT([planimetria,linea])
    
    
    planimetria=OFFSET([0.1,0.4,1.5])(planimetria)
    planimetria=OFFSET([-0.1,-0.2,0])(planimetria)
    
    return planimetria 
    
def ggpl_svgParetiI(file):
    planimetria=QUOTE([0])
    with open(file, 'rb') as csvFile:
        reader = csv.DictReader(csvFile)
        righe=csv.reader(csvFile, delimiter=' ',quotechar='|')
        for riga in righe:
            l=listFromString(riga[0])
            linea=MKPOL([[[l[0],l[1],0],[l[2],l[3],0]],[[1,2]],[1]])
            planimetria=STRUCT([planimetria,linea])
    
    planimetria=OFFSET([0.15,0.15,3.5])(planimetria)
    
    c=PROD([QUOTE([2]),QUOTE([2])])
    d=PROD([c,QUOTE([50])])
    planimetria=DIFFERENCE([planimetria,d])
    
    return planimetria 
    
def ggpl_svgFacciataE(file):
    facciata=QUOTE([0])
    c = 0
    with open(file, 'rb') as csvFile:
        reader = csv.DictReader(csvFile)
        righe=csv.reader(csvFile, delimiter=' ',quotechar='|')
        for riga in righe:
            if c <= 1:
                l1 = listFromString(riga[0])
                linea1 = MKPOL([[[l1[0],l1[1],0],[l1[2],l1[3],0]],[[1,2]],[1]])
                facciata=STRUCT([facciata,linea1])
            else: break
            c += 1
    
    facciata=OFFSET([0.15,0.15,3.5])(facciata)
    
    return facciata
    
def ggpl_svgParetiE(file):
    planimetria=QUOTE([0])
    with open(file, 'rb') as csvFile:
        reader = csv.DictReader(csvFile)
        righe=csv.reader(csvFile, delimiter=' ',quotechar='|')
        for riga in righe:
            l=listFromString(riga[0])
            linea=MKPOL([[[l[0],l[1],0],[l[2],l[3],0]],[[1,2]],[1]])
            planimetria=STRUCT([planimetria,linea])
    
    planimetria=OFFSET([0.3,0.3,3.5])(planimetria)
    
    c=PROD([QUOTE([2]),QUOTE([2])])
    d=PROD([c,QUOTE([50])])
    planimetria=DIFFERENCE([planimetria,d])
    
    return planimetria
    
def creaTetto(tettoSolido):
    listavertici1=UKPOL(tettoSolido)
    tettoPiano=OFFSET([0.2,0.2,-0.2])(tettoSolido)
    tettoPiano=T(3)(0.2)(tettoPiano)
    tettoPiano=COLOR(RED)(tettoPiano)
    scheletro=SKEL_1(tettoSolido)
    scheletroSpesso=OFFSET([0.2,0.2,-0.5])(scheletro)
    scheletroSpesso=COLOR(BROWN)(scheletroSpesso)
    finale=STRUCT([scheletroSpesso,tettoPiano])

    return finale
    
def creaCombinationRoof():
    tettoFacce=MKPOL([[[0,0,0],[6,0,0],[0,12,0],[6,12,0],[2,3,2],[2,9,2],[4,3,2],[4,9,2],[3,6,3.5]],[[1,3,5,6],[3,4,6,8],[4,2,8,7],[2,1,5,7],[5,6,9],[6,8,9],[8,7,9],[7,5,9]],1])
    tettoFacce=OFFSET([0,0,0.01])(tettoFacce)
    return tettoFacce
    
def creaPavimento(x,y,z):
    pavimento=MKPOL([[[x+1.26,y+9,z],[x+1.26,y+21.7,z],[x+19,y+9,z],[x+19,y+21.7,z]],[[1,2,3,4]],[1]])
    pavimento=OFFSET([0,0,-0.1])(pavimento)

    return pavimento
    
def ggpl_MyHouse():
    finestre=ggpl_svgFinestre("finestre.lines")
    porte=ggpl_svgPorte("porte.lines")
    paretiE=ggpl_svgParetiE("pareti_esterne.lines")
    paretiI=ggpl_svgParetiI("pareti_interne.lines")
    finestre=T(3)(1)(finestre)
    pareti=STRUCT([paretiE,paretiI])
    pavimento=creaPavimento(0,0,0)
    bucoScala=MKPOL([[[8.3,10,0],[8.3,11.5,0],[11,10,0],[11,11.5,0]],[[1,2,3,4]],[1]])
    bucoScala=OFFSET([0,0,-0.1])(bucoScala)
    pavimento=DIFFERENCE([pavimento,bucoScala])
    pareti_finestre=DIFFERENCE([pareti,finestre])
    pareti_finestre_porte=DIFFERENCE([pareti_finestre,porte])
    scala= designStairs(1.5,3.5,3.5)
    scala=R([1,2])(PI/2)(scala)
    scala=T(1)(15)(scala)
    scala=T(2)(10)(scala)
    finestre2=ggpl_svgFinestre2("finestre.lines")
    finestre2=T(3)(1)(finestre2)
    finestre2=TEXTURE(["vetro3.png",True,False,1,1,0,1,1])(finestre2)
    porte2=ggpl_svgPorte2("porte.lines")
    porte2=COLOR(Color4f([139/255.,69/255.,19/255.,1]))(porte2)
    r1=MKPOL([[[1.26,9,0],[1.26,9,1.3],[1.26,11.5,0],[1.26,11.5,1.3]],[[1,2,3,4]],[1]])
    r2=MKPOL([[[1.26,9,0],[1.26,9,1.3],[19,9,0],[19,9,1.3]],[[1,2,3,4]],[1]])
    r3=MKPOL([[[19,9,0],[19,9,1.3],[19,21.7,0],[19,21.7,1.3]],[[1,2,3,4]],[1]])
    r4=MKPOL([[[19,21.7,0],[19,21.7,1.3],[17,21.7,0],[17,21.7,1.3]],[[1,2,3,4]],[1]])

    INTERNE=DIFFERENCE([paretiI,porte])
    ESTERNE=DIFFERENCE([paretiE,porte])
    ESTERNE=DIFFERENCE([ESTERNE,finestre])
    ESTERNE=TEXTURE(["mattone-rivestimento-venice-color-gold-di-rondine.jpg",True,False,1,1,PI/8,100,4])(ESTERNE)
    PARETI=STRUCT([INTERNE,ESTERNE])
    pareti_finestre_porte=STRUCT([PARETI,pavimento,scala,r1,r2,r3,r4,finestre2,porte2])
    
    return pareti_finestre_porte

def ggpl_ultimopiano():
    
    pavimento=creaPavimento(0,0,0)
    bucoScala=MKPOL([[[8.3,10,0],[8.3,11.5,0],[11,10,0],[11,11.5,0]],[[1,2,3,4]],[1]])
    bucoScala=OFFSET([0,0,-0.1])(bucoScala)
    pavimento=DIFFERENCE([pavimento,bucoScala])
    r1=MKPOL([[[1.26,9,0],[1.26,9,1.3],[1.26,21.7,0],[1.26,21.7,1.3]],[[1,2,3,4]],[1]])
    r2=MKPOL([[[1.26,9,0],[1.26,9,1.3],[19,9,0],[19,9,1.3]],[[1,2,3,4]],[1]])
    r3=MKPOL([[[19,9,0],[19,9,1.3],[19,21.7,0],[19,21.7,1.3]],[[1,2,3,4]],[1]])
    r4=MKPOL([[[19,21.7,0],[19,21.7,1.3],[1.26,21.7,0],[1.26,21.7,1.3]],[[1,2,3,4]],[1]])


    pareti_finestre_porte=STRUCT([pavimento,r1,r2,r3,r4])
    return pareti_finestre_porte

def piani():
    primo= ggpl_MyHouse()
    secondo =ggpl_MyHouse()
    secondo=T(3)(3.5)(secondo)
    terzo=ggpl_MyHouse()
    terzo=T(3)(7)(terzo)
    quarto =ggpl_MyHouse()
    quarto=T(3)(10.5)(quarto)
    quinto =ggpl_MyHouse()
    quinto=T(3)(14)(quinto)
    ultimo=ggpl_ultimopiano()
    ultimo=T(3)(17.5)(ultimo)
    tetto=creaCombinationRoof()
    tetto2=creaTetto(tetto)
    tetto2=T(3)(19.2)(tetto2)
    tetto2=R([1,2])(PI/2)(tetto2)
    tetto2=T(1)(13.1)(tetto2)
    tetto2=T(2)(4.2)(tetto2)
    tetto2=S(1)(1.45)(tetto2)
    tetto2=S(2)(2.1)(tetto2)
    casa=STRUCT([primo, secondo, terzo, quarto, quinto,ultimo,tetto2])
    
    return casa
    
def piani3():
    primo= ggpl_MyHouse()
    secondo =ggpl_MyHouse()
    secondo=T(3)(3.5)(secondo)
    ultimo=ggpl_ultimopiano()
    ultimo=T(3)(7)(ultimo)
    tetto=creaCombinationRoof()
    tetto2=creaTetto(tetto)
    tetto2=T(3)(8.7)(tetto2)
    tetto2=R([1,2])(PI/2)(tetto2)
    tetto2=T(1)(13.1)(tetto2)
    tetto2=T(2)(4.2)(tetto2)
    tetto2=S(1)(1.45)(tetto2)
    tetto2=S(2)(2.1)(tetto2)
    casa=STRUCT([primo, secondo,ultimo,tetto2])
    
    return casa
    
def singoloN():
    nord=piani()
    return nord
    
def singoloS():
    sud=piani()
    sud=R([1,2])(PI/2)(sud)
    sud=R([1,2])(PI/2)(sud)
    sud=T(1)(20.3)(sud)
    sud=T(2)(43.7)(sud)
    return sud
    
def doppio():
    nord=piani()
    sud=piani()
    sud=R([1,2])(PI/2)(sud)
    sud=R([1,2])(PI/2)(sud)
    sud=T(1)(20.3)(sud)
    sud=T(2)(43.7)(sud)
    struct=STRUCT([nord,sud])
    return struct