import numpy as np
import matplotlib.pyplot as plt

def plot(x, fx, a):
    xplt = []
    fxplt = []
    step = (x[-1]-x[0])/1000
    for t in np.arange(x[0], x[-1]+step, step):
        p = 0
        for i in range(len(a)):
            p += a[i]*t**i
        fxplt.append(p)
        xplt.append(t)

    plt.plot(x, fx, "x", label="pontos")
    plt.plot(xplt, fxplt, 'r-', label="curva de ajuste")
    plt.ylabel('gráfico')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.ion()
    plt.legend()
    plt.show()
    input("...pressione enter...")
    plt.close()

def ex1():
    x = np.array([0.11, 0.56, 1.31, 2.04, 2.85, 3.64, 4.6, 5.38, 6.32])
    fx = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
    z = np.polyfit(x, fx, 2)
    z = np.flip(z)
    print("Coeficientes do polinomio: ", z)
    plot(x, fx, z)

# EXEMPLO DO VIDEO 3 SOBRE AJUSTE DE CURVAS:
def ex_vid3():
    w1 = 0.3*np.pi
    w2 = 20*np.pi
    tau = 0.15
    beta = 0.2
    t = np.arange(0, 2*np.pi, np.pi/200 )
    s = np.sin(w1*t)+tau*np.cos(w2*t) * np.exp(-beta*t)
    z = np.flip(np.polyfit(t, s, 3))
    plot(t, s, z)