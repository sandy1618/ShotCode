import matplotlib.pyplot as plt
import numpy as np
#from scipy.optimize import curve_fit
from scipy.stats import linregress

	

def refraction1d(filename,graph=0):
	'''This function read a file with interpreted seismic first arrivals and returns a 
	1d velocity model
	If graph=1 this will plot the curve fit results and the 1d estimated model'''
	
	M=np.loadtxt(filename)
	
	i=0
	nlayers=int(M[0][0])
	picks=M[1:nlayers+1][:]
	M2=M[nlayers+1:][:]
	j=0
	vdm=np.zeros(nlayers,2)
	while i<nlayers:
		while M2[j][0]<picks[i][0]:
			j=j+1
			if M2[j][0]>=picks[i][0]:
				if i==0:
					refrax=M2[0:j][0]
					refray[j]=M2[0:j][1]
					ja=j
					#estimate velocity
				else:
					refrax=M2[ja:j][0]
					refray[j]=M2[ja:j][1]
					ja=j
					#estimate velocity and depth
			
		
		i=i+1
		

	if graph==1:
		print("teste")
	else:
		print("nothing")
