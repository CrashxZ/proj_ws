import json
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = plt.axes(projection="3d")

with open('coordinates.json') as file:
    for line in file:
        _pathData = json.loads(line)
        x = [_pathData['x']]
        y = [_pathData['y']]
        z = [_pathData['z']]
        ax.scatter(x, y, z, c='b', marker='.', linewidths=0.01)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('Flight Data')
plt.grid(True)
plt.show()
