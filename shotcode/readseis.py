#from obspy.io.seg2.seg2 import _read_seg2

import numpy as np
from obspy.io.segy.segy import _read_su


def read_su2d(data):
	"""Reads a Seismic Unix data file
	input:
		data: is a string with your data name
	output:
		sdata: matrix where each column represents a seismic trace
		header: a dictionary with header words"""


	st=_read_su(data)


	#Get information from traces
	ns = len(st.traces[0].data)
	tracl=len(st.traces) #number of traces
	dt=(st.traces[0].header.sample_interval_in_ms_for_this_trace)/1000000 # sampling rate in seconds
	ft=(dt*ns)-dt #final time in seconds

	header={"dt":dt,"ns":ns,"tracl":tracl}

	#Write the data into a matrix

	dado=np.zeros((tracl, ns)) #empty matrix where I write the data
	i=0

	while i<tracl:
    		dado[i][:]=st.traces[i].data
    		i=i+1
    
	sdata=np.transpose(dado)


	return(sdata,header)


