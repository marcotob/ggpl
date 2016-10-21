<<<<<<< HEAD
from pyplasm import *

# xPil altezza trave
# yPil profondita trave
# xBeam larghezza pilastro
# zBeam profondita pilastro

def fun(xPil,yPil,xBeam,zBeam,ldy,lhz):
    
	pilx=QUOTE([xPil,0])
	pily=QUOTE([yPil,0])
	pillar=PROD([pilx,pily])
	pillarS=STRUCT([QUOTE([0])])
	height=0
	for h in lhz:
		newPillar=PROD([pillar,QUOTE([h])])
		pillarS=STRUCT([pillarS,T(3)(-height)(newPillar)])
		dist=0	
		for d in ldy:
			dist=-d-xPil+dist
			pillarS=STRUCT([pillarS,T([1,3])([-dist,-height])(newPillar)])
		height=height-h-xBeam
		
	beamx=QUOTE([xBeam,0])
	beamz=QUOTE([zBeam,0])
	beamS=STRUCT([QUOTE([0])])
	height=0
	a=0
	endPillar=PROD([PROD([pilx,pily]),beamz])
	for h in lhz: 
		height=height-h-a
		dist = 0
		for d in ldy:
			newBeam=PROD([PROD([QUOTE([d+xPil]),beamz]),beamx])
			beamS=STRUCT([beamS,T([1,3])([-dist,-height])(newBeam)])	
			dist=dist-d-xPil
		beamS=STRUCT([beamS,T([1,3])([-dist,-height])(endPillar)])
		a=xBeam
	
	struct=STRUCT([pillarS,beamS])
	return struct

l=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1]
l2=[0.1,0.2,0.1,0.3]
l3=[0.4,0.2,0.4,0.2]
struttura=fun(0.01,0.02,0.01,0.02,l3,l3)
VIEW(struttura)
=======
from pyplasm import *

# xPil altezza trave
# yPil profondita trave
# xBeam larghezza pilastro
# zBeam profondita pilastro

def fun(xPil,yPil,xBeam,zBeam,ldy,lhz):
    
	pilx=QUOTE([xPil,0])
	pily=QUOTE([yPil,0])
	pillar=PROD([pilx,pily])
	pillarS=STRUCT([QUOTE([0])])
	height=0
	for h in lhz:
		newPillar=PROD([pillar,QUOTE([h])])
		pillarS=STRUCT([pillarS,T(3)(-height)(newPillar)])
		dist=0	
		for d in ldy:
			dist=-d-xPil+dist
			pillarS=STRUCT([pillarS,T([1,3])([-dist,-height])(newPillar)])
		height=height-h-xBeam
		
	beamx=QUOTE([xBeam,0])
	beamz=QUOTE([zBeam,0])
	beamS=STRUCT([QUOTE([0])])
	height=0
	a=0
	endPillar=PROD([PROD([pilx,pily]),beamz])
	for h in lhz: 
		height=height-h-a
		dist = 0
		for d in ldy:
			newBeam=PROD([PROD([QUOTE([d+xPil]),beamz]),beamx])
			beamS=STRUCT([beamS,T([1,3])([-dist,-height])(newBeam)])	
			dist=dist-d-xPil
		beamS=STRUCT([beamS,T([1,3])([-dist,-height])(endPillar)])
		a=xBeam
	
	struct=STRUCT([pillarS,beamS])
	return struct

l=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1]
l2=[0.1,0.2,0.1,0.3]
l3=[0.4,0.2,0.4,0.2]
struttura=fun(0.01,0.02,0.01,0.02,l3,l3)
VIEW(struttura)
>>>>>>> d91e028028ce2956caf6cd436700b1693191e117
