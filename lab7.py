import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
m=int(input('enter number of rows in m*n array'))
n=int(input('enter number of columns in m* array'))
x=np.random.randint(10,size=(m,n))
print(x)
objects=("Rows","cols","dims","size","Items","nBts")
y_pos=np.arange(len(objects))
attributes=[m,n,x.ndim,x.size,x.itemsize,x.nbytes]
plt.bar(y_pos,attributes,align="center",alpha=0.5)
plt.xticks(y_pos,objects)
plt.ylabel("count")
plt.title(f"attribute of (m)X(n) array")
plt.show()
