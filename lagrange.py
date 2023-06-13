from polynomial import Polynomial
import numpy.polynomial.polynomial as poly 
class LagrangeBase:
    F:Polynomial = None
    def __init__(self,xarr,yarr):
        phyrexiaArray = []
        for i in range(len(xarr)):
            phyrexia = Polynomial(params=[1])
            divisor = 1
            currx = xarr[i]
            for j in range(len(xarr)):
                if(i != j):
                    xi = xarr[j]
                    temp = Polynomial(params=[xi*-1,1])
                    phyrexia *= temp
                    divisor *= (currx - xi)
            
            print(str(i) + ': ' + str(phyrexia) + '/' + str(divisor))
            phyrexia = phyrexia/divisor
            print(phyrexia)
            phyrexiaArray.append(phyrexia)

        F = Polynomial(order=0)
        for i in range(len(yarr)):
            F += phyrexiaArray[i] * yarr[i]
        
        self.F = F
        print('F: ' + str(F))
    
    def val(self,x):
        return self.F.val(x)
    
