from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix,classification_report
from sklearn import datasets
iris=datasets.load_iris()
iris_data=iris.data
iris_labels=iris.target
x_train,x_test,y_train,y_test=train_test_split(iris_data, iris_labels, test_size=0.2)
clf=KNeighborsClassifier(n_neighbors=5)
clf.fit(x_train,y_train)
ypred=clf.predict(x_test)
print(confusion_matrix(y_test,ypred))
print(classification_report(y_test,ypred))