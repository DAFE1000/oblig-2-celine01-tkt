import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

#Funksjonen fra oppgaven
def f(x):
    return np.exp(-x/4) * np.arctan(x)

#Linkningen som bestemmer topppunktet
def g(x):
    return np.arctan(x) - 4 / (x**2 + 1)

#Finn x-verdien til topppunktet numerisk
x_start = 1.5
x_top = fsolve(g, x_start) [0]

#Finn y-verdien
y_top = f(x_top)

#Skriv ut svaret
print(f"x-top =  {x_top:.6f}")
print(f"y-top = {y_top:.6f}")

#Lag plott
x = np.linspace(-4,6,500)
y = f(x)

plt.figure(figsize=(8,5))
plt.plot(x, y, label=r"4f(x)=e^{-x/4}\arctan(x)$")
plt.scatter(x_top, y_top, label=f"Toppunkt ({x_top:.4f}, {y_top:.4f})")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Plot av funksjonen med toppunkt")
plt.grid(True)
plt.legend()

#Lagre plottet i plots-mappen
plt.savefig("plot.png")
plt.show()

