import matplotlib.pyplot as plt
plt.style.use('classic')
import pandas as pd
import numpy as np
import seaborn as sns
rng=np.random.RandomState(0)
x=np.linspace(0,10,500)
y=np.cumsum(rng.randn(500,6),0)
sns.set()
plt.plot(x,y)
plt.legend('ABCDEF',ncol=2, loc='upper left');
plt.title('DAta in seaborns default style')
plt.show()
data=np.random.multivariate_normal([0,0],[[5,2],[2,2]],size=200)
data=pd.DataFrame(data,columns=['x','y'])
for col in 'xy':
    sns.kdeplot(data[col], shade=True)
plt.title('kernel density and histogram plotted together using distplot')
plt.show()

sns.kdeplot(data.x,data.y);
plt.title("a 2 dimensional kernel density plot")
plt.show()

with sns.axes_style('white'):
    sns.jointplot("x","y",data,kind='kde');

plt.title('joint distribution plot')
plt.show()
iris=sns.load_dataset("iris")
print(iris.head())

sns.pairplot(iris,hue='species',height=3);
plt.title('A pair plot showing the relationships between four variables')
plt.show()

tips=sns.load_dataset('tips')
print(tips.head())
tips['tip_pct']=100*tips['tip']/tips['total_bill']
grid=sns.FacetGrid(tips,row="sex",col="time",margin_titles=True)
grid.map(plt.hist,"tip_pct",bins=np.linspace(0,40,15));
plt.title('faceted histogram')
plt.show()

with sns.axes_style(style='ticks'):
    g=sns.factorplot("day","total_bill","sex",data=tips,kind="box")
g.set_axis_labels("day","Total bill");
plt.title('factor plot')
plt.show()

with sns.axes_style('white'):
    sns.jointplot("total_bill","tip",data=tips,kind="hex")
plt.title('joint distribution plot')
plt.show()
