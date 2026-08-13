import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle

fig, ax = plt.subplots(figsize=(8,8))
ax.add_patch(Ellipse((-2, 1.5), 3.5, 5, angle=30,
                     edgecolor='black', facecolor='violet'))
ax.add_patch(Ellipse((-2, -1.5), 2.8, 4, angle=-20,
                     edgecolor='black', facecolor='pink'))
ax.add_patch(Ellipse((2, 1.5), 3.5, 5, angle=-30,
                     edgecolor='black', facecolor='violet'))
ax.add_patch(Ellipse((2, -1.5), 2.8, 4, angle=20,
                     edgecolor='black', facecolor='pink'))

ax.add_patch(Ellipse((0, 0), 0.8, 6,
                     edgecolor='black', facecolor='black'))
ax.add_patch(Circle((0, 3.4), 0.4,
                    edgecolor='black', facecolor='black'))
ax.plot([0, -0.8], [3.7, 5], color='black')
ax.plot([0, 0.8], [3.7, 5], color='black')
for x in [-2, 2]:
    ax.add_patch(Circle((x, 1.5), 0.3,
                        edgecolor='yellow', facecolor='yellow'))
    ax.add_patch(Circle((x, -1.5), 0.25,
                        edgecolor='white', facecolor='white'))
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.set_aspect('equal')
ax.grid(True)
ax.set_title("Butterfly")

plt.show()