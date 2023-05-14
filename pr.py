from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
import numpy as np

x1 = np.arange(0.0, 1.1, 0.1)
after_molar_Volume = np.array([2.000, 1.738, 1.544, 1.406, 1.312, 1.250, 1.208, 1.174, 1.136, 1.082, 1.000])
molar_Volume1 = 1
molar_Volume2 = 2

def molar_Volume(x1) :
    return (molar_Volume1 - molar_Volume2) * x1 + (molar_Volume2)
def mix_molar_Volume(x1) :
    return after_molar_Volume - molar_Volume(x1)

def pi_coef(x1) :
    return mix_molar_Volume(x1) / (x1 * (1-x1))

print(pi_coef(x1))

x = np.arange(0.0, 1.1, 0.1)[:, np.newaxis]
y = np.array(mix_molar_Volume(x1))

pr = LinearRegression()

quadratic = PolynomialFeatures(degree=2)
x_quad = quadratic.fit_transform(x)

x_fit = np.arange(0, 1.1, 0.1)[:, np.newaxis]

pr.fit(x_quad, y)
print("coef : ", pr.coef_)
print("intercept : ", pr.intercept_)
y_quad_fit = pr.predict(quadratic.fit_transform(x_fit))

plt.figure(1)
plt.scatter(x, y, label='sample')
#plt.plot(x_fit, y_quad_fit, label='quadratic fit')
#plt.plot(x_fit, -0.856*(x1)+1*x1**2-0.072, label='Reg_get graph')
plt.plot(x1, x1*(1-x1)**2*(-2), label='difference of mix molar Volume')
plt.legend()

x2 = 1
w1 = -0.856
w0 = -0.072

plt.figure(2)
plt.plot(x1, -2*(1-x1)**2*(1-2*x1) + molar_Volume1, label="Partial molar Volume 1")
plt.plot(x1, -4*(x1)**2*(1-x1) + molar_Volume2, label='Partial molar Volume 2')

##plt.figure(1)
##plt.plot(x1, molar_Volume(x1), x1, after_molar_Volume)
##plt.figure(2)
##plt.plot(x1, mix_molar_Volume(x1))
plt.legend()
plt.show()

