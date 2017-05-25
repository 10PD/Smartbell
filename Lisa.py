#LISA - Puts the Smart in Dumbell
import numpy as np
from random import randint
import matplotlib.pyplot as plt
#from sklearn import tree


def normalise(data):
    x = list()
    y = list()
    for item in data:
        norm_x = item[0]
        norm_y = item[1]
        x.append(item[0]-norm_x)
        y.append(item[1]-norm_y)
    return x,y

#Takes 2d array of last_x and last_y (from Output.py)
#Returns a list of two polynomails. x,y = [0],[1]
def polyRegress(data):
    x, y = normalise(data)
    
    #Finds polynomial for X movement
    z = np.polyfit(x, range(0,len(x)), 5)
    polyX = np.poly1d(z)

    #Finds polynomial for Y movement
    q = np.polyfit(y, range(0,len(y)), 5)
    polyY = np.poly1d(q)

    
    return [polyX, polyY]


#Generates example data of 50 samples
#X is 'slowly moving upwards'
#Y is 'slightly moving side-to-side' for random variance
last_x = list()
last_y = list()
for i in range(50,100):
    rdm = randint(1,5)
    last_x.append(i+rdm)
    last_y.append(rdm)
example_data = [last_x, last_y]

z = np.polyfit(last_x, range(0,len(last_x)), 5)
polyX = np.poly1d(z)

print(polyX)
#polyList = polyRegress(example_data)

























# calculate new x's and y's
##print("calc new")
##x_newX = np.linspace(x[0], x[-1], 50)
##x_newY = polyX(x_newX)
##
##y_newX = np.linspace(y[0], y[-1], 50)
##y_newY = polyY(y_newX)
##
##print("plotting")
##plt.plot(y,y_newX,'o',y_newX, y_newY)
###plt.plot(x,x_newX,'o',x_newX, x_newY)
##plt.xlim([x[0]-1, x[-1] + 1 ])
##plt.show()

##plt.plot(x_new)
##plt.show()

#Accuracy example
#from sklearn.metrics import accuracy_score
#predictions = clf.predict(features)
#print(accuracy_score(labels, predictions))

#Dumps the AI's brain!
#from sklearn.externals import joblib
#import pickle
#joblib.dump(clf, "Brains/Hello.pkl")
