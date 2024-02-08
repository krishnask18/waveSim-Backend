from sympy import *

t = Symbol('t', real=True)
w = Symbol('w', real=True)

# class Signal:
#     def Integrate(self, domain=t, l=-oo, u=oo):
#         return integrate(self(domain), (domain, l, u))
#     def ctft(self):
#         return integrate(self(t)*exp(-1j*t*w), (t, -oo, oo)).simplify()

class impulse:
    def __init__(self, t):
        self.name = "impulse"
        self.t = t
    def __call__(self, t_ = None):
        if t_ == None:
            t_ = self.t
        return DiracDelta(t_)
    def __repr__(self):
        return f"{self()}"
    # def __mul__(self, other):
    #     try:
    #         return self()*other()
    #     except:
    #         return self()*other
    
class step:
    def __init__(self, t):
        self.name = "step"
        self.t = t
    def __call__(self, t_ = None):
        if t_ == None:
            t_ = self.t
        return Heaviside(t_, 1)
    def __repr__(self):
        return f"{self()}"
    
class Exp:
    def __init__(self, t):
        self.name = "exp"
        self.t = t
    def __call__(self, t_ = None):
        if t_ == None:
            t_ = self.t
        return exp(t_)
    def __repr__(self):
        return f"{self()}"

# class gate:


def a_t0(arg):
    a = diff(arg, t)
    t0 = solve(arg/a, t)[0]
    return a, t0


def ctft(func, bounds=(-oo, oo)):
    a, t0 = a_t0(func.t)
    if func.name == "step":
        return (((pi*DiracDelta(w)+1/(1j*w)).simplify()).subs(w, w/a)*(exp(-1j*t0*w)/abs(a))).simplify()
    return ((integrate(func(t)*exp(-1j*t*w), (t, bounds[0], bounds[1])).simplify()).subs(w, w/a)*(exp(-1j*t0*w)/abs(a))).simplify()

# pretty_print(ctft(Exp(t), bounds=(-oo,0)).args[0][0])
# pretty_print(impulse(t-1)(t))
print(isinstance(impulse(t), step))
print(isinstance(t, Symbol))
# pretty_print(ctft(step(t-1)))
# pretty_print(ctft_step(step(-t-1).t))
# p1 = plot(abs(ctft(step(t))), show=False)
# p1.show()