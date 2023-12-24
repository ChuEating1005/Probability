import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Parameters
lambda_ = 0.08  # Example rate
T = 0.08        # Example time window
c_values = np.linspace(1, 1000, 1000)  # Range of c values

# Functions
def markov_bound(c):
    return 1 / c

def chebyshev_bound(c, lambda_, T):
    return 1 / (((c - 1) ** 2) * lambda_ * T) if c > 1 else np.inf

def chernoff_bound(c, lambda_, T):
    return np.exp(c * lambda_ * T * (1 - np.log(c) - 1 / c) );

# Calculate values
p_values = [1 - poisson.cdf(c * lambda_ * T, lambda_ * T) for c in c_values]
markov_values = [markov_bound(c) for c in c_values]
chebyshev_values = [chebyshev_bound(c, lambda_, T) for c in c_values]
chernoff_values = [chernoff_bound(c, lambda_, T) for c in c_values]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(c_values, p_values, label='P(X > cλT)', color='blue')
plt.plot(c_values, markov_values, label='Markov Bound', color='red')
plt.plot(c_values, chebyshev_values, label='Chebyshev Bound', color='green')
plt.plot(c_values, chernoff_values, label='Chernoff Bound', color='purple')

plt.xlabel('c')
plt.ylabel('Probability / Bound')
plt.title('Probability and Bounds for Poisson Random Variable')
plt.legend()
plt.yscale('log')  # Log scale for better visibility
plt.ylim(0, 1)
# plt.savefig(f"./figures/p1.png", dpi=300)
plt.show()