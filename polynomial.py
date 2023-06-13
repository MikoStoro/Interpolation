import numpy as np

class Polynomial:
    order = 0
    parameters = []
    
    def val(self,arg):
        ret = 0
        for i in range(self.order):
            ret += self.parameters[i] * pow(arg,i)
        return ret
    
    def __init__(self, order:int=None, params:list=[]):
        if order != None:
            self.order = order
        else:
            self.order = len(params)
        self.parameters = np.zeros(self.order)
        for i in range(len(params)):
            self.parameters[i] = params[i]
        
    def __mulPoly(self,other):
        ret = Polynomial(order=(self.order + other.order -1))
        for i in range(self.order):
            for j in range(other.order):
                ret.parameters[i+j] += self.parameters[i] * other.parameters[j]
        return ret

    def __mulNum(self, other):
        parameters = np.zeros(self.order)
        for i in range(self.order):
            parameters[i] = self.parameters[i] * other
        return Polynomial(params=parameters)

    def __mul__(self, other):
        if type(other) is Polynomial:
            return self.__mulPoly(other)
        else:
            return self.__mulNum(other)

    def __pow__(self,other):
        ret = Polynomial(params=[1])
        for _ in range(other):
           ret = ret * self
        return ret 


    def __add__(self,other):
        newOrder = max([self.order,other.order])
        ret = Polynomial(order=newOrder)
        for i in range(newOrder):
            if self.order > i:
                ret.parameters[i] += self.parameters[i]
            if other.order > i:
                ret.parameters[i] += other.parameters[i]
        return ret

    def __truediv__(self,other):
        parameters = np.zeros(self.order)
        for i in range(self.order):
            parameters[i] = self.parameters[i] / other
        return Polynomial(params=parameters)

    def __str__(self) -> str:
        ret = ''
        for i in range(self.order-1, -1, -1):
            ret += str(self.parameters[i])
            if i > 0:
                ret += ('x' + str(i) + ' + ')
        return ret
