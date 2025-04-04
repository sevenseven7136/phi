def Tau(f): #タウ変換
    def g(x):
        return f(f(x))
    return g

def Phi(f,n): #ファイ変換
    if n==0:
        return f
    else:
        return Phi(f,n-1)(f)

def f_0(x):
    return x**x

def phi_l(x): #小ファイ関数
    return Phi(Phi(Tau,x),x)(f_0)(x)

def phi_L(x): #大ファイ関数
    def Phi_x(f):
        return Phi(f,x)
    t = Tau
    for i in range(x):
        t = Phi_x(t)
    return t(f_0)(x)

def phi_L_v2(x): #大ファイ関数v2
    def Phi_x(f):
        return Phi(f,x)
    return Phi_x(Tau)(Phi_x)(Tau)(f_0)(x)

def Phi_S(f,g,n): #強ファイ変換
    if n==0:
        return g(f)
    else:
        return Phi_S(f,g,n-1)(g)(f)

def phi_LL(x): #強大ファイ関数
    def Phi_x(f):
        return Phi(f,x)
    return Phi_S(Tau,Phi_x,x)(f_0)(x)