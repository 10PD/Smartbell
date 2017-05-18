#LISA - Puts the Smart in Dumbell
#WinPy application
from sklearn import tree

#Sample dataset
features = [[140, 1], [130, 1], [150, 0], [170, 0], [135, 2], [132, 2], [137, 2]]
#Ordered labels for dataset
labels = [0, 0, 1, 1, 2, 2, 2]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
check = [[133, 2]]
print ( clf.predict(check) )
print ( clf.decision_path(check) )

#Graphing example
#import matplotlib.pyplot as plt
#plt.plot(features)
#plt.show()

#Accuracy example
#from sklearn.metrics import accuracy_score
#predictions = clf.predict(features)
#print(accuracy_score(labels, predictions))

#Dumps the AI's brain!
#from sklearn.externals import joblib
#import pickle
#joblib.dump(clf, "Brains/Hello.pkl")
