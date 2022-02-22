import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import seaborn; seaborn.set()
data=pd.read_csv('fremont-bridge.csv',index_col="Date",parse_dates=True)
data.columns=['west','east']
data['total']=data.eval('west+east')
print(data.dropna().describe())
data.plot()
plt.ylabel("Hourly  bicycle count");
plt.show()
weekly=data.resample('W').sum()
weekly.plot(style=[':','--','-'])
plt.ylabel("weekly bicycle count");
plt.show()
daily=data.resample('D').sum()
daily.rolling(30,center=True).sum().plot(style=[':','--','-',])
plt.ylabel("mean hourly count");
plt.show()
by_time=data.groupby(data.index.time).mean()
hourly_ticks=4*60*60*np.arange(6)
by_time.plot(xticks=hourly_ticks,style=[':','--','-']);
plt.title("Average hourly bicycle counts")
plt.show()
by_weekday=data.grouphy(data.index.dayofdweek).mean()
by_weekday.index=['Mon','Tues','Wed','Thurs','Fri','Sat','Sun']
by_weekday.plot(style=[':','--','-']);
plt.title("average daily bicycle counts")
