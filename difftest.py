from sympy import symbols, diff
v1, v2, n1, n2, n = symbols('v1 v2 n1 n2 n', imaginary=True)
#v = -0.1 * v1 * v2 / (v1 + v2) * n1 * n2 / n + n1 * v1 + n2 * v2
#v1_hat = diff(v, n1)
#v2_hat = diff(v, n2)
#print(v1_hat)
#print(v2_hat)

v = -2*(n1*n2**2)/((n1+n2)**2) + n1*v1 + n2*v2
v1_hat = diff(v, n1)
print(v1_hat)
v2_hat = diff(v, n2)
print(v2_hat)