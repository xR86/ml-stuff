import numpy as np
import matplotlib.pyplot as mat

x = np.linspace(0, np.pi, 32)
fig = mat.figure()
fig.plot(x, np.sin(x))
fig.savefig('sine.png')