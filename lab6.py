import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
fig=plt.figure()
ax=plt.axes()
x=np.linspace(0,10,1000)
plt.plot(x, np.sin(x - 0),color='blue')
plt.plot(x, np.sin(x - 1),color='green')
plt.plot(x, np.sin(x - 2),color='red')
plt.plot(x, np.sin(x - 3),color='cyan')
plt.plot(x, np.sin(x - 4),color='y')
plt.plot(x, np.sin(x - 5),color='k');
plt.title('a simple line plot')
plt.show()
rng=np.random.RandomState(0)
x=rng.randn(100)
y=rng.randn(100)
colors=rng.randn(100)
y=rng.randn(100)
colors=rng.randn(100)
sizes=1000*rng.rand(100)
plt.scatter(x,y,c=colors, s=sizes,alpha=0.3, cmap='viridis')
plt.colorbar();
plt.title("scatter plot")
plt.show()
def f(x,y):
    return np.sin(x) ** 10 +np.cos(10+y*x) * np.cos(x)
x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 40)
X,Y=np.meshgrid(x,y)
Z=f(X,Y)
plt.contourf(X,Y,Z,20, cmap="RdGy")
plt.colorbar()
plt.title("countour plot")
plt.show()
data=np.random.randn(100)
plt.hist(data,bins=30, alpha=0.5,histtype="stepfilled",color="steelblue", edgecolor="none");
plt.title('histogram')
plt.show()
mean=[0,0]
cov=[[1,1],[1,2]]
x,y=np.random.multivariate_normal(mean,cov,10000).T
plt.hist2d(x,y,bins=30,cmap="Blues")
cb=plt.colorbar()
cb.set_label("counts in bin")
plt.title("2 dimensional histogram")
plt.show()

                
