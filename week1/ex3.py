import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import svm, metrics

df = pd.read_csv('ex2data1.txt',header=None)
df.columns = ['test1','test2','pass']
notPassed = df[df['pass'] == 0]
passed = df[df['pass'] == 1]
plt.plot(notPassed['test1'],notPassed['test2'],'yo')
plt.plot(passed['test1'],passed['test2'],'bo')
plt.show()

X = df[['test1','test2']]
y = df['pass']

# h = .01
h = 1
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=0)
neigh = KNeighborsClassifier(n_neighbors=3).fit(X_train,y_train)
print (neigh.score(X_train, y_train),neigh.score(X_test, y_test))
# x_min, x_max = df['test1'].min() - 3, df['test1'].max() + 3
# y_min, y_max = df['test2'].min() - 3, df['test2'].max() + 3
x_min, x_max = df['test1'].min() - .2, df['test1'].max() + .2
y_min, y_max = df['test2'].min() - .2, df['test2'].max() + .2
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                        np.arange(y_min, y_max, h))
Z = neigh.predict(np.c_[xx.ravel(), yy.ravel()])
# PREDICTED = neigh.predict(X_test)
# metrics.classification_report(y_test,PREDICTED)

# Put the result into a color plot
Z = Z.reshape(xx.shape)
plt.pcolormesh(xx, yy, Z, cmap=cmap_light)
plt.plot(notPassed['test1'],notPassed['test2'],'yo')
plt.plot(passed['test1'],passed['test2'],'bo')
plt.show()