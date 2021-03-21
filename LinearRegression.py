import math
class LinearRegression:

    def __init__(self,iX, iY):
        self.x = iX
        self.y = iY
        self.n = len(self.x)
        self.x_sum = sum(self.x)
        self.y_sum = sum(self.y)

    def x_y_sum(self):
        return sum(self.x[i]*self.y[i] for i in range(self.n))
    
    def y_y_sum(self):
        return sum(self.y[i]**2 for i in range(self.n))
    
    def x_x_sum(self):
        return sum(self.x[i]**2 for i in range(self.n))

    #!MUDAR os a_a_sum para esta função
    def calc_sum(self,a,b,n):
        return sum(a*b for i in range(n))

    def m(self):
        return ((self.n*self.x_y_sum())-(self.x_sum*self.y_sum))/((self.n*self.x_x_sum())-(self.x_sum**2))

    def b(self):
        return ((self.x_x_sum()*self.y_sum)-(self.x_sum*self.x_y_sum()))/((self.n*self.x_x_sum())-(self.x_sum**2))

    def r2(self):
        return (((self.n*self.x_y_sum())-(self.x_sum*self.y_sum))**2)/(((self.n*self.x_x_sum())-(self.x_sum**2))*((self.n*self.y_y_sum())-(self.y_sum**2)))

    def deltaM(self):
        return abs(self.m())*math.sqrt(((1/self.r2())-1)/(self.n-2))

    def deltaAB(self):
        return self.deltaM() * math.sqrt(self.x_x_sum()/self.n)

    def __repr__(self):
        txt = "MSF Regressão Linear Library\n\n"
        txt +="*-*-*-*-*-*-*-*-*-*-*-*-*-*\n"
        txt += f"X   = [{self.x}]\n"
        txt += f"Y   = [{self.y}]\n"
        txt += f"m   = {self.m()}\n"
        txt += f"b   = {self.b()}\n"
        txt += f"R^2 = {self.r2()}\n"
        txt += f"dM  = {self.deltaM()}\n"
        txt += f"dAB = {self.deltaAB()}"
        return txt
    
    def getTuple(self):
        return (self.m(),self.b(),self.r2(),self.deltaM(),self.deltaAB())