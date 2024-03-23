from random_walk import RandomWalk
from matplotlib import pyplot as plt

walk = RandomWalk(50000)
walk.fill_walk()

plt.style.use('grayscale')
fig, ax = plt.subplots()

(x_values, y_values) = walk.get_walk()
indices = range(len(x_values))

# Data
ax.scatter(x_values,y_values, c=indices, cmap=plt.cm.Blues, s=1) # Colormap

# Ticklabel parameters
ax.ticklabel_format(style='plain')

# Set chart title and label axes.
ax.set_title("Random Walk", fontsize=24)
ax.set_xlabel("Position X", fontsize=14)
ax.set_ylabel("Position Y", fontsize=14)
ax.axis([min(x_values), max(x_values), min(y_values), max(y_values)])

# Set size of tick labels.
ax.tick_params(labelsize=14)
plt.savefig('random_walk.png',bbox_inches='tight')
plt.show()