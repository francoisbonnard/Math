import numpy as np
import plyplot as plt

x4=np.linspace(-10,10)
y4=np.sqrt(x**3/(x-1))
y5=y4-x4
y6=y4+x4
plt.plot(x4,y4)
plt.plot(x4,y5)
plt.plot(x4,y6)

# 2+(x+1)e-2x