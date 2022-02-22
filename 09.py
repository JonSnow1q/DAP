import matplotlib.pyplot as plt 
import numpy as np 
from sklearn.linear_model import LogisticRegression 
from sklearn.metrics import classification_report, confusion_matrix 
plt.style.use("seaborn-whitegrid") 
x = np.arange(10).reshape(-1, 1) 
y = np.array([0,0,0,0,1,1,1,1,1,1]) 
model = LogisticRegression(solver='liblinear',random_state=0) 
model.fit(x, y) 
print(f"classes: {model.classes_}") 
intercept=model.intercept_ 
print(f"intercept is {intercept}") 
slope=model.coef_ 
print(f"slope is {slope}") 
y_new=model.predict_proba(x) 
print(f"prediction probability {y_new}") 
y_pred=model.predict(x) 
print(f"predictions{y_pred}") 
sc=model.score(x, y) 
print(f"accuracy of the model {sc}") 
con_mat=confusion_matrix(y, model.predict(x)) 
print("confusion matrix") 
print(con_mat) 
print("") 
plt.plot(x,y_pred,"o",color="green") 
plt.plot(x,y_new[:,1],"-s",color="gray") 
y1=[0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5] 
plt.plot(x,y1) 
plt.show()
