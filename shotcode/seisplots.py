from scipy.fftpack import fft
import matplotlib.pyplot as plt
import numpy as np
from obspy.signal.util import next_pow_2




#Wiggle plots
def wigb(data,t_axis,offsets,amx):
	''' This function plots seismic traces as wiggle plot
	data: Is a matrix of seismic data where the columns are the seismic traces
	t_axis: Is your time axis
	offsets: vector of each trace offset 
	amx: is a screen gain to the data'''
	amx2=amx*np.max(data)
	i=0
	for offset in offsets:
		
		x=np.divide(data[:,i],amx2)+offset
		i=i+1
		
		plt.plot(x,t_axis,'k')
		plt.fill_betweenx(t_axis,offset,x,where=(x>offset),color='k')

	plt.ylabel('Time (s)')
	plt.xlabel('Offset (m)')
	plt.xlim((offsets[0]-1.,offsets[-1]+1.))
	plt.ylim((0.0,t_axis[-1]))
	plt.gca().invert_yaxis()
	#plt.show()
	
	
	
def pick_wigb(data,t_axis,offsets,filename,amx):
	''' This function enables picking and saving on a seismic wiggle plot
	data: Is a matrix of seismic data where the columns are the seismic traces
	t_axis: Is your time axis
	offsets: vector of each trace offset 
	filename: Is the output filename
	amx: is a screen gain to the data'''
	amx2=amx*np.max(data)
	i=0
	for offset in offsets:
		
		x=np.divide(data[:,i],amx2)+offset
		i=i+1
		
		plt.plot(x,t_axis,'k')
		plt.fill_betweenx(t_axis,offset,x,where=(x>offset),color='k')

	plt.ylabel('Time (s)')
	plt.xlabel('Offset (m)')
	plt.gca().invert_yaxis()
	plt.xlim((offsets[0]-1.,offsets[-1]+1.))
	picks = plt.ginput( n=0, timeout=0, show_clicks=True, mouse_add=1, mouse_pop=3, mouse_stop=2)
	np.savetxt(filename, picks)
	plt.show()


def interpret_refract(name):
	'''Select the maximum time each event is observed'''
	
	
		
	M=np.loadtxt(name)

	x=M[:,0]
	t_axis=M[:,1]
	plt.plot(x,t_axis,'k.-')
	plt.ylabel('Time (s)')
	plt.xlabel('Offset (m)')
	picks = plt.ginput( n=0, timeout=0, show_clicks=True, mouse_add=1, mouse_pop=3, mouse_stop=2)
	plt.show()
	ninterfaces=len(picks) #number of layers
	M2=np.array([ninterfaces,0])
		
	M4=np.vstack([M2,picks,M])
	filename="r_"+name
	np.savetxt(filename, M4)

def ampli_spec(D,header):
	'''Plots the amplitude spectrum for each seismic trace of data matrix D
	in a same graph'''

	dt=header["dt"]
	nx=header['tracl']
	ns=header['ns']
	k=next_pow_2(ns)
	nf=4*(2^k)
	
	t=np.linspace(0.0,ns*dt,ns)
	tf=np.linspace(0.0,1.0/(2*dt),nf/2)
	i=0
	while i<nx:
		df=fft(D[:,i],nf)
		i=i+1
		plt.plot(tf,2.0/dt*np.abs(df[0:int(nf/2)]))
		

	plt.ylabel('Amplitude')
	plt.xlabel('Frequency (Hz)')
	plt.grid()
	plt.show()









