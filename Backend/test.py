from sympy.integrals.transforms import fourier_transform
import sympy as sm
from sympy import integrate, exp, pi, oo, Heaviside, DiracDelta, pretty_print, cos, sin
import matplotlib.pyplot as plt
import numpy as np

def plot(exp):
    t_ = np.linspace(0, 10, 1000)
    f = []
    for _ in t_:
        f.append(exp.subs(w, _))
    plt.plot(t_, np.abs(f))
t = sm.Symbol('t', real = True)
w = sm.Symbol('w', real = True)
j = 1j
# pretty_print(fourier_transform(cos(2*pi*t), t, 1))
pretty_print(integrate((exp(-t**2)*exp(-1j*w*t)), (t,-oo, oo)))

# p1 = plot(abs(integrate((cos(2*pi*3*t)+cos(2*pi*t))*exp(-j*2*pi*t*w), (t, -oo, oo)).args[0][0]))
# p1 = plot((integrate((cos(2*pi*t)+cos(2*pi*4*t))*exp(-j*2*pi*t*w), (t, -oo, oo)).args[0][0]))

# plt.show()