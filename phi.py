def Tau(f):
    def g(x):
        return f(f(x))
    return g

def Phi(f,n):
    if n==0:
        return f
    else:
        return Phi(f,n-1)(f)

def f_0(x):
    return x**x

def phi_l(x):
    return Phi(Phi(Tau,x),x)(f_0)(x)

def phi_L(x):
    def Phi_x(f):
        return Phi(f,x)
    t = Tau
    for i in range(x):
        t = Phi_x(t)
    return t(f_0)(x)
