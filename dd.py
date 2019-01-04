# proprietary to BEERA // DO NOT COPY



import numpy as np

n = np.arange(36)

n.resize(6,6)

m=n.reshape(36)[::7]


print(m)