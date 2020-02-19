import extraction
import os
from primary_colors import prim
from compliment_colors import comp
import matplotlib as plot

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')

#size = pts.shape[0]
#for i in range(size):
#    ax.plot([pts[i, 0]], [pts[i, 1]], [pts[i, 2]], '.',
#            color=(pts[i, 3], pts[i, 4], pts[i, 5]), markersize=8, #alpha=0.5)

for p in :
    ax.plot([p[0]], [p[1]], [p[2]], '.', color=(p[3], p[4], p[5]),  
            markersize=8, alpha=0.5)  

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()