import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Define the initial condition g(x) for x >= 0
def g(x):
    return (x/(1+x**2))**2

# Numerically compute the inverse function g^{-1}(u)
def g_inv(u):
    # Solve g(x) - u = 0 for x, starting with an initial guess
    sol = fsolve(lambda x: g(x) - u, np.sqrt(u) if u > 0 else 0.1)
    return sol[0]

# Create an array of u values within the range of g (0 to 1/4)
u_vals = np.linspace(0.001, 0.25, 100)
# Compute g^{-1}(u) for these u values
x0_vals = np.array([g_inv(u) for u in u_vals])

# Compute the derivative (g^{-1})'(u) using finite differences
dg_inv_du = np.gradient(x0_vals, u_vals)

# Compute the shock time for each u (with f''(u)=1)
t_vals = -dg_inv_du

# Identify the minimum shock time and corresponding u (inflection point of g^{-1})
min_index = np.argmin(t_vals)
t_shock = t_vals[min_index]
u_inflection = u_vals[min_index]
x_inflection = x0_vals[min_index]

print(f"Shock forms first for u = {u_inflection:.4f} at time t = {t_shock:.4f}")

# Plot characteristic lines: x = u*t + g^{-1}(u)
t = np.linspace(0, t_shock*1.5, 200)
plt.figure(figsize=(8,6))
for u in u_vals[::5]:  # Plot a subset for clarity
    x0 = g_inv(u)
    x = u*t + x0
    plt.plot(t, x, 'b-', alpha=0.3)

# Mark the envelope point
plt.plot(t_shock, u_inflection*t_shock + g_inv(u_inflection), 'ro', markersize=8,
         label=f'First shock at t={t_shock:.2f}')

plt.xlabel('t')
plt.ylabel('x')
plt.title('Characteristic Lines for g(x)=[x/(1+x^2)]^2')
plt.legend()
plt.grid(True)
plt.show()
