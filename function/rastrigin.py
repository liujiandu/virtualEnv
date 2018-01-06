#!coding=utf-8
import numpy as np

A = 10.0
def func(x):
	sum = 0.0
	n = x.shape[0]
	for i in range(n):
		sum+=(x[i]**2 - A*np.cos(2*np.pi*x[i]))
	return A*n+sum

def gfunc(x):
	return 2*x+A*2*np.pi*np.sin(x)

if __name__=="__main__":
        import sys
        sys.path.append('../')
        from tool.plot import plot3d
        plot3d(func, np.array([9, 13]), np.array([17, 20]))
	#print rastrigin(np.array([[1.0, 0.0], [3.0,0.0]]))

