import numpy as np
import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7,8,9,10]
y=[11,12,13,14,15,16,17,18,19,20]

arthx=np.mean(x)
arthy=np.mean(y)

devx = np.std(x) / np.sqrt(len(x) - 1)
devy = np.std(y) / np.sqrt(len(y) - 1)

print(arthx)
print(arthy)
print(devx)
print(devy)

