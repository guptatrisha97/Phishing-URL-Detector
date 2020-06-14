# -- coding: utf-8 --


#----------------importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
from imblearn.ensemble import BalancedRandomForestClassifier

class RandomForest:

	#importing the dataset
	dataset = pd.read_csv("datasets/phishcoop.csv")
	dataset = dataset.drop('id', 1) #removing unwanted column


<<<<<<< HEAD
	X = dataset.iloc[0:5,[6,14]].values
	y = dataset.iloc[0:5,30].values
	#split features and label into training ang testing data
	from sklearn.model_selection import train_test_split
	X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=4)
	#perform feature scaling
	from sklearn.preprocessing import StandardScaler
	scalar = StandardScaler()
	X_train = scalar.fit_transform (X_train)
	X_test = scalar.transform (X_test)

	classifier = RandomForestClassifier(n_estimators = 100, criterion = "gini", max_features = 'log2',  random_state = 0)
	classifier.fit(X_train, y_train)

	#predicting the tests set result
	y_pred = classifier.predict(X_test)
	print(classifier.score(X_test, y_test))

=======
#spliting the dataset into training set and test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.14, random_state =0 )

#----------------applying grid search to find best performing parameters
from sklearn.model_selection import GridSearchCV
parameters = [{'n_estimators': [100, 700],
    'max_features': ['sqrt', 'log2'],
    'criterion' :['gini', 'entropy']}]

grid_search = GridSearchCV(RandomForestClassifier(),  parameters,cv =5, n_jobs= -1)
grid_search.fit(x_train, y_train)
#printing best parameters
print("Best Accurancy =" +str( grid_search.best_score_))
print("best parameters =" + str(grid_search.best_params_))
#-------------------------------------------------------------------------

#fitting RandomForest regression with best params
classifier = BalancedRandomForestClassifier(n_estimators = 100, criterion = "gini", max_features = 'log2',  random_state = 0 , class_weight = 'balanced')
classifier.fit(x_train, y_train)
>>>>>>> b57b169535b57c497d9e244b4ddd8785e0632966

	x = dataset.iloc[ : , :-1].values
	y = dataset.iloc[:, -1:].values

	#spliting the dataset into training set and test set
	from sklearn.model_selection import train_test_split
	x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.14, random_state = 4 )

	#----------------applying grid search to find best performing parameters 
	from sklearn.model_selection import GridSearchCV
	parameters = [{'n_estimators': [100, 700],
	    'max_features': ['sqrt', 'log2'],
	    'criterion' :['gini', 'entropy']}]

<<<<<<< HEAD
	grid_search = GridSearchCV(RandomForestClassifier(),  parameters,cv =5, n_jobs= -1)
	grid_search.fit(x_train, y_train)
	#printing best parameters 
	print("Best Accurancy =" +str( grid_search.best_score_))
	print("best parameters =" + str(grid_search.best_params_)) 
	#-------------------------------------------------------------------------
=======
#pickle file joblib
joblib.dump(classifier, '../final_models/rf_final.pkl')
>>>>>>> b57b169535b57c497d9e244b4ddd8785e0632966

	#fitting RandomForest regression with best params 
	classifier = RandomForestClassifier(n_estimators = 100, criterion = "gini", max_features = 'log2',  random_state = 0)
	classifier.fit(x_train, y_train)

	#predicting the tests set result
	y_pred = classifier.predict(x_test)

	#confusion matrix
	from sklearn.metrics import confusion_matrix
	cm = confusion_matrix(y_test, y_pred)
	print(cm)


	#pickle file joblib
	#joblib.dump(classifier, 'final_models/rf_final.pkl')


	#-------------Features Importance random forest
	names = dataset.iloc[:,:-1].columns
	importances =classifier.feature_importances_
	sorted_importances = sorted(importances, reverse=True)
	indices = np.argsort(-importances)
	var_imp = pd.DataFrame(sorted_importances, names[indices], columns=['importance'])



	#-------------plotting variable importance
	plt.title("Variable Importances")
	plt.barh(np.arange(len(names)), sorted_importances, height = 0.7)
	plt.yticks(np.arange(len(names)), names[indices], fontsize=7)
	plt.xlabel('Relative Importance')
	plt.show()
