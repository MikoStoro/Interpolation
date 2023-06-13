from polynomial import Polynomial
import numpy as np

class SplineInterpolation:
    segments = []
    xvalues = []
    parameters = []

    def __init__(self, xarr, yarr):
        segmentCount = len(xarr) -1
        A = np.zeros((segmentCount*4,segmentCount*4))
        r = np.zeros((segmentCount*4))
        self.xvalues = xarr
        row = 0
        for s in range(segmentCount):
            a0 = s * 4
            b0 = a0+1
            c0 = b0+1
            d0 = c0+1
            x0 = xarr[s]
            x1 = xarr[s+1]
            diff = x1 - x0
            c1 = c0+4
            b1 = b0 + 4
            
            #S(x0) = f(xo)
            A[row][a0] = 1
            r[row] = yarr[s]
            row += 1
            #S(x1) = f(x1)
            A[row][a0] = 1
            A[row][b0] = diff
            A[row][c0] = diff**2
            A[row][d0] = diff**3
            r[row] = yarr[s+1]
            row += 1
            if s == 0:
                #S''(x0) = 0
                A[row][c0] = 2
                r[row] = yarr[s]
                row += 1
                #S''(x1) = S(i+1)''(x1)
                A[row][c0]=2
                A[row][d0]= 6*diff
                A[row][c1] = -2
                r[row]=0
                row +=1
                #S'(x1) = S(i+1)'(x1)
                A[row][b0] = 1
                A[row][c0] = 2*diff
                A[row][d0]=3*(diff**2)
                A[row][b1] = -1
                r[row] = 0
                row += 1
            elif s == segmentCount-1:
              #S''(x1) = 0
                A[row][c0] = 2
                A[row][d0] = 6*diff
                r[row] = 0 
            else:
                 #S''(x1) = S(i+1)''(x1)
                A[row][c0]=2
                A[row][d0]= 6*diff
                A[row][c1] = -2
                r[row]=0
                row +=1
                #S'(x1) = S(i+1)'(x1)
                A[row][b0] = 1
                A[row][c0] = 2*diff
                A[row][d0]=3*(diff**2)
                A[row][b1] = -1
                r[row] = 0
                row += 1
        
        self.parameters = np.linalg.solve(A, r)

    def val(self,x):
        if x < self.xvalues[0] or x > self.xvalues[-1]:
            print('x out of range!')
            return None
        for i in range(len(self.xvalues)-1):
            if x >= self.xvalues[i] and x <= self.xvalues[i+1]:
                a = self.parameters[i*4]
                b = self.parameters[i*4+1]
                c = self.parameters[i*4+2]
                d = self.parameters[i*4+3]
                temp = Polynomial(params=[a,b,c,d])
                xval = x - self.xvalues[i] 
                print('x: ' + str(x) + ' y: ' + str(temp.val(xval)) + ' S: ' + str(i))
                return temp.val(xval)
