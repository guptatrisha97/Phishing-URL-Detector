# -*- coding: utf-8 -*-

#importing libraries
from sklearn.externals import joblib
import inputScript
import imaplib, email
import os, pkg_resources
import importlib.resources as pkg_resources
#load the pickle file
classifier = joblib.load('final_models/rf_final.pkl')

#input url
print("Checking...")
#url = input()
def extractURL(fileName):

    wordsInLine = []
    tempWord = []
    urlList = []

    #open up the file containing the email
    file = open(fileName)
    for line in file:
        #create a list that contains each word in each line
        wordsInLine = line.split(' ')
        #For each word try to split it with :
        for word in wordsInLine:
            tempWord = word.split(":")
            #Check to see if the word is a URL
            if len(tempWord) == 2:
                if tempWord[0] == "http" or tempWord[0] == "https":
                    urlList.append(word)

    file.close()

    return urlList[0]
#checking and predicting
checkprediction = inputScript.main(extractURL('email.txt'))
prediction = classifier.predict(checkprediction)
if (prediction == 1):
    print("Email contains URL that may be a phishing attack!")
else:
    print("Email contains URL that seems safe")
