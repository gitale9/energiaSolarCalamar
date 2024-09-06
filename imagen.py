import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots()

# Estructura con paneles solares
structure = patches.Rectangle((0.1, 0.6), 0.2, 0.2, linewidth=1, edgecolor='black', facecolor='lightgrey')
ax.add_patch(structure)
ax.text(0.15, 0.8, 'Paneles Solares', fontsize=10, ha='center')
ax.plot([0.2, 0.2], [0.6, 0.55], 'k-')  # Varilla de puesta a tierra
ax.text(0.25, 0.55, 'Varilla de Puesta a Tierra', fontsize=8, ha='left')

# Casa
house = patches.Rectangle((0.4, 0.2), 0.5, 0.5, linewidth=1, edgecolor='black', facecolor='lightgrey')
ax.add_patch(house)
ax.text(0.65, 0.65, 'Casa', fontsize=10, ha='center')

# Gabinete con equipos
cabinet = patches.Rectangle((0.5, 0.4), 0.1, 0.1, linewidth=1, edgecolor='blue', facecolor='lightblue')
ax.add_patch(cabinet)
ax.text(0.55, 0.45, 'Gabinete', fontsize=8, ha='center')

# Bombillos y tomacorrientes
ax.plot([0.5, 0.55], [0.3, 0.3], 'ko')  # Bombillo
ax.text(0.55, 0.3, 'Bombillo', fontsize=8, ha='left')
ax.plot([0.7, 0.75], [0.3, 0.3], 'ks')  # Tomacorriente
ax.text(0.75, 0.3, 'Tomacorriente', fontsize=8, ha='left')

# Tablero eléctrico
panel = patches.Rectangle((0.7, 0.4), 0.1, 0.1, linewidth=1, edgecolor='red', facecolor='pink')
ax.add_patch(panel)
ax.text(0.75, 0.45, 'Tablero', fontsize=8, ha='center')

# Ajustes finales
plt.xlim(0, 1)
plt.ylim(0, 1)
ax.set_aspect('equal', adjustable='box')
plt.axis('off')
plt.title('Esquema del Sistema Fotovoltaico')

# Mostrar la imagen
plt.show()
