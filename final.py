import matplotlib.pyplot as plt
import numpy as np

x1 = np.arange(0.0, 1.1, 0.1)
after_molar_Volume = np.array([2.000, 1.738, 1.544, 1.406, 1.312, 1.250, 1.208, 1.174, 1.136, 1.082, 1.000])
molar_Volume1 = 1
molar_Volume2 = 2
def delta_molar_Volume(x1):
    return x1*(1-x1)**2*(-2)

print(delta_molar_Volume(x1))

def molar_Volume(x1):
    return delta_molar_Volume(x1) + x1*molar_Volume1 + (1-x1)*molar_Volume2

delta_molar_volume = delta_molar_Volume(x1)
molar_volume = molar_Volume(x1)

plt.figure(1)
plt.ylim(-0.5, 2)
plt.plot(x1, delta_molar_volume, label='difference of mix molar Volume')
plt.plot(x1, molar_volume, label='Molar Volume')

def partial_molar_Volume1(x1):
    return molar_Volume1 - (2 * (1-x1)**2 * (1-2*x1))
def partial_molar_Volume2(x1):
    return molar_Volume2 - (4 * x1**2 * (1-x1))

plt.figure(2)
plt.plot(x1, partial_molar_Volume1(x1), label = 'Partial Molar Volume 1')
plt.plot(x1, partial_molar_Volume2(x1), label = 'Partial Molar Volume 2')
plt.legend()
plt.show()
