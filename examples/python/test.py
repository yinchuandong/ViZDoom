import numpy as np


p = [1.26073303e-07, 8.44543369e-09, 9.99999762e-01, 1.03947151e-09,
     2.05525555e-10, 2.46727611e-10, 8.39249523e-08, 3.28854699e-09]
p = np.array(p)

mean = 1.0 / len(p)

print 'sum:', np.sum(p)
print 'mean:', mean 
print np.array(p > mean)
