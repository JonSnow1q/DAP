import matplotlib.pyplot as plt
plt.style.use('classic')
import numpy as np
import pandas as pd
import seaborn as sns
# Create some data
rng = np.random.RandomState(0)
x = np.linspace(0, 10, 500)
y = np.cumsum(rng.randn(500, 6), 0)
sns.set()#set the style by calling Seaborn’s set() method
plt.plot(x, y)
plt.legend('ABCDEF', ncol=2, loc='upper left');
plt.title('Data in Seaborn’s default style')
plt.show()
data = np.random.multivariate_normal([0, 0], [[5, 2], [2, 2]], size=2000)
data = pd.DataFrame(data, columns=['x', 'y'])
for col in 'xy':
    sns.kdeplot(data[col], shade=True)
plt.title('Kernel density estimates for visualizing distributions')
plt.show()
sns.distplot(data['x'])
sns.distplot(data['y']);
plt.title('Kernel density and histograms plotted together using distplot')
plt.show()
#If we pass the full two-dimensional dataset to kdeplot,
#we will get a two-dimensional visualization of the data
sns.kdeplot(data.x,data.y);
plt.title("A two-dimensional kernel density plot")
plt.show()
#We can see the joint distribution and the marginal
#distributions together using #sns.jointplot
with sns.axes_style('white'): #white background
    sns.jointplot("x", "y", data, kind='kde');
#A joint distribution plot with a two-dimensional kernel
#density estimate
plt.title('Joint distribution plot')
plt.show()
iris = sns.load_dataset("iris")
#lists measurements of petals and sepals of three iris species
print(iris.head())
#joint plots for  datasets of larger dimensions generate
#pair plots. useful in exploring correlations between
#multidimensional data.
#plot all pairs of values against each other
sns.pairplot(iris, hue='species', height=3);
plt.title('A pair plot showing the relationships between four variables')
plt.show()
#view data via histograms of subsets using FacetGrid
#data that shows the amount that restaurant staff receive
#in tips based on various indicator data
tips = sns.load_dataset('tips')
print(tips.head())
tips['tip_pct'] = 100 * tips['tip'] / tips['total_bill']
grid = sns.FacetGrid(tips, row="sex", col="time", margin_titles=True)
grid.map(plt.hist, "tip_pct", bins=np.linspace(0, 40, 15));
plt.title('faceted histogram')
plt.show()
#Factor plots
with sns.axes_style(style='ticks'):
    g = sns.factorplot("day", "total_bill", "sex", data=tips, kind="box")
g.set_axis_labels("Day", "Total Bill");
plt.title('Factor plot')
plt.show()
#Joint distribution
with sns.axes_style('white'):
    sns.jointplot("total_bill", "tip", data=tips, kind='hex')
plt.title('joint distribution plot')
plt.show()
