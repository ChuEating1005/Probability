import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import multivariate_normal

# Define the mean and covariance matrix for the bivariate distribution
mean = [0, 0]
cov = [[1, 0.5], [0.5, 1]]  # Diagonal covariance, points are uncorrelated

# Create a grid of (x, y) values
x, y = np.mgrid[-3:3:.01, -3:3:.01]
pos = np.dstack((x, y))

# Create a multivariate normal distribution
rv = multivariate_normal(mean, cov)

# Create a 3D axis for plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(x, y, rv.pdf(pos), cmap='viridis', linewidth=0)

# Add labels and title
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('PDF')
ax.set_title('Bivariate Normal Distribution')

# Show the plot
plt.show()
