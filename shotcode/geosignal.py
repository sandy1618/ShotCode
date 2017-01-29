from scipy.fftpack import fft,ifft
import numpy as np
import matplotlib.pyplot as plt
from obspy.signal.util import next_pow_2
import scipy



def filterfx(D,header,f,c=0):
	'''Apply a band pass filkter for each seismic trace of data matrix D
	with phase rotation c'''

	dt=header["dt"]
	nx=header['tracl']
	ns=header['ns']
	k=next_pow_2(ns)
	nf=4*(2^k)
	pi=np.pi
	t=np.linspace(0.0,ns*dt,ns)
	tf=np.linspace(0.0,1.0/(2*dt),nf/2)
	i=0
	DF=np.zeros([2*len(tf),nx])
	

	sf1=np.floor(nf*f[0]*dt)+1 
	sf2=np.floor(nf*f[1]*dt)+1
	sf3=np.floor(nf*f[2]*dt)+1
	sf4=np.floor(nf*f[3]*dt)+1

	up=np.linspace(0,sf2-sf1-1,sf2-sf1)/(sf2-sf1)
	down=np.linspace(sf4-sf3-1,0,sf4-sf3)/(sf4-sf3)
	
	aux=np.hstack((np.zeros(int(sf1)),up,np.ones(int(sf3-sf2)),down,np.zeros(int((nf/2)-sf4))))
	aux2=np.fliplr([aux])[0]

	F=np.hstack((aux,aux2))
	Phase=(pi/180.0)*np.hstack([0.0,-c*np.ones(int(nf/2)-1),0.0,c*np.ones(int(nf/2)-1)])
	Transfer=F*np.exp(-1j*Phase)
	
	DF=fft(D,nf,0)
	
	
	R=Transfer[:,None]*DF
	
	o=ifft(R,nf,0)
	o=np.real(o[0:ns,:])
	return o
	


def convmtx(w, n):
	'''Creates a convolution matrix
	w: is the wavelet
	n: is the number of samples from the reflectivity which we want to conlvove the wavelet'''
	
	column=np.hstack((w[0],np.zeros(n-1)))
	row=np.hstack((w,np.zeros(n-1)))
	return scipy.linalg.toeplitz(row,column)









