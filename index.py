# -*- coding: utf-8 -*-

#importing libraries
import joblib
import inputScript
import imaplib, email
import os, pkg_resources
import importlib.resources as pkg_resources
from whiteBlacklist import WhiteBlackApp
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
                if tempWord[0] == "http" or tempWord[0] == "https" or tempWord[0] == "www":
                    urlList.append(word)

    file.close()
    if(len(urlList)==0):
        print ("Email has no URL")
        return None
    else:
        return urlList
#checking and predicting
if (extractURL('email.txt') == None):
    print("Email does not contain a URL")
else:
    urlValue = []
    urlValue = extractURL('email.txt')
    length = len(urlValue)
    for i in range(length):
        checkprediction = inputScript.main(urlValue[i])
<<<<<<< HEAD
        white_black_test = WhiteBlackApp(urlValue[i], self.domain)
        white_black_results = white_black_test.run()
        if white_black_results[0]:
=======
        prediction = classifier.predict(checkprediction)
        #print (prediction)
        if (prediction == 1):
>>>>>>> b57b169535b57c497d9e244b4ddd8785e0632966
            print("Email contains URL that may be a phishing attack: " + urlValue[i])
        elif white_black_results[1]:
            print("Email contains URL that seems safe: " + urlValue[i])
        prediction = classifier.predict(checkprediction)
        else:
            if (prediction == 1):
                print("Email contains URL that may be a phishing attack: " + urlValue[i])
            else:
                print("Email contains URL that seems safe: " + urlValue[i])
