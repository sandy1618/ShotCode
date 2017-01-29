import numpy as np





def gvmodel(v,h,dh,modname,nx,nz,plotg=0):
	'''Generates a 2d model given the vertical proprierties vector 'v' and
	a depths vector 'h' 
	dh: grid_spacing - dx=dz=dh
	modname: model name
	nx: number of points in the horizontal
	nz: is the number of points in the vertical'''
	
	mod=np.zeros([nz,nx])
	i=0
	while i<=len(v):
		if i==0:
			mod[0:int(h[0]/dh),:]=v[0]
		elif i==len(v):
			mod[int(h[1]/dh):,:]=v[2]
		else:
			mod[int(h[0]/dh):int(h[1]/dh),:]=v[1]
		
		i=i+1

	# Write binary data to a file
	with open(modname, 'wb') as f:
    		f.write(mod)
	f.close()
	
	
	if plotg==1:
		import matplotlib.pyplot as plt
		vecz=np.linspace(0,dh*nz,nz)
		vecx=np.linspace(0,dh*nx,nx)
		plt.imshow(mod,cmap="jet",extent=[0,dh*nx,dh*nz,0])
		plt.colorbar()
		plt.xlabel('Distance (m)')
		plt.ylabel('Depth (m)')
		plt.show()
