class IntSpace:
    def __init__(self,f,x):
        self.f = f
        self.x = x
    
    def F(self,_):
        self.x = self.f(self.x)
        return self
    
    def Tau(self,g,*args):
        for i in range(self.x):
            g(*args)
        return self
    
    def Phi(self,g,h):
        g(*(g for i in range(self.x)),h)
        return self

    def getX(self):
        return self.x

def succ(x): return x+1

def phi(x):
    space = IntSpace(succ,x)
    return space.Phi(space.Tau,space.f).getX()