import numpy.polynomial.polynomial as poly 
class LagrangeBase:
    F:poly.Polynomial = None
    def __init__(self,xarr,yarr):
        phyrexiaArray = []
        for i in range(len(xarr)):
            phyrexia = poly.Polynomial([1])
            divisor = 1
            currx = xarr[i]
            for j in range(len(xarr)):
                if(i != j):
                    xi = xarr[j]
                    temp =  poly.Polynomial([xi*-1,1])
                    phyrexia *= temp
                    divisor *= (currx - xi)
            
            print(str(i) + ': ' + str(phyrexia) + '/' + str(divisor))
            phyrexia = phyrexia/divisor
            print(phyrexia)
            phyrexiaArray.append(phyrexia)

        F =  poly.Polynomial([0])
        for i in range(len(yarr)):
            F += phyrexiaArray[i] * yarr[i]
        self.F = F
        print('F: ' + str(F))
    
    def val(self,x):
        return self.F(x)