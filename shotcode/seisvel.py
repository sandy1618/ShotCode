import numpy as np


def hyperbola(v,x,t0):
	t=np.sqrt(np.power(t0,2)+(np.power(x,2)/np.power(v,2)))
	return t
