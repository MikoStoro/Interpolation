import polynomial
from spline import SplineInterpolation
from lagrange import LagrangeBase
from visualize import visualize
from extract import extractData


ypoints = [1, 4, 6, 8, 10, 8, 10, 8, 10, 15, 20, 23, 26]
xpoints = [1,2,3,4,5,6,7,8,9,10,11,12,13]
x1 = [308.6,362.6,423.3,491.4]
y1 = [0.055389,0.047485, 0.040914, 0.035413]

x = [1,3,5]
y = [6,-2,4]
s = SplineInterpolation(xarr=xpoints,yarr=ypoints)
visualize(s,0,26,0.1)
x = [0,2,3,4]
y = [4,1,6,1]

x1=[3, 4, 5, 6, 7, 8, 9, 10, 11]
y1= [0.024, 0.035, 0.046, 0.058, 0.067, 0.083, 0.097, 0.111, 0.125]
based = LagrangeBase(xarr=x1,yarr=y1)
visualize(based,start=x1[0],end=x1[-1])