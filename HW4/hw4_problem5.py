#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sample code of HW4 Problem 5

"""

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

N = 10000000
mu = 0
repeat = 100

Delta_A_list = []

#-------- Your code (~10 lines) ----------

for _ in range(repeat):
    # Generate random points
    x = np.random.uniform(-1, 1, N)
    y = np.random.uniform(-1, 1, N)

    # Check if the points are inside the region
    inside = ((x - 0.25)**2 + 2 * (y + 0.5)**2 <= 0.25) & (x + y <= 0)

    # Estimate the area
    area_estimate = 4 * np.sum(inside) / N
    Delta_A_list.append(area_estimate)

#---------- End of your code -----------
# Optional: Print the Monte-Carlo estimates abnd visualize the empirical CDF
print(Delta_A_list)
ecdf = stats.cumfreq(Delta_A_list, numbins=25)
x = ecdf.lowerlimit + np.linspace(0, ecdf.binsize*ecdf.cumcount.size, ecdf.cumcount.size)

fig, ax = plt.subplots()
ax.bar(x, ecdf.cumcount / len(Delta_A_list), width=ecdf.binsize)
ax.set_title('Empirical CDF')
ax.set_xlabel('Estimated Delta_A')
ax.set_ylabel('Cumulative Frequency')
plt.savefig(f"./figures/p5_N={N}_repeat={repeat}.png", dpi=300)