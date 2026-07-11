import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle

fig, ax = plt.subplots(figsize=(8,8))

# Left Wings
ax.add_patch(Ellipse((-2, 1.5), 3.5, 5, angle=30,
                     edgecolor='black', facecolor='violet'))
ax.add_patch(Ellipse((-2, -1.5), 2.8, 4, angle=-20,
                     edgecolor='black', facecolor='pink'))

# Right Wings
ax.add_patch(Ellipse((2, 1.5), 3.5, 5, angle=-30,
                     edgecolor='black', facecolor='violet'))
ax.add_patch(Ellipse((2, -1.5), 2.8, 4, angle=20,
                     edgecolor='black', facecolor='pink'))

# Body
ax.add_patch(Ellipse((0, 0), 0.8, 6,
                     edgecolor='black', facecolor='black'))

# Head
ax.add_patch(Circle((0, 3.4), 0.4,
                    edgecolor='black', facecolor='black'))

# Antennae
ax.plot([0, -0.8], [3.7, 5], color='black')
ax.plot([0, 0.8], [3.7, 5], color='black')

# Decorations on wings
for x in [-2, 2]:
    ax.add_patch(Circle((x, 1.5), 0.3,
                        edgecolor='yellow', facecolor='yellow'))
    ax.add_patch(Circle((x, -1.5), 0.25,
                        edgecolor='white', facecolor='white'))

# Graph settings
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.set_aspect('equal')
ax.grid(True)
ax.set_title("Butterfly")

plt.show()