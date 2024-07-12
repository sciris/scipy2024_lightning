import numpy as np
np.random.seed(1)

import numpy as np
import sciris as sc

with sc.timer():
    raw = np.random.rand(20,20)
    smooth = sc.gauss2d(raw, scale=2)
    sc.bar3d(smooth, cmap='orangeblue')

sc.savefig('sciris-scipy-showcase.png')