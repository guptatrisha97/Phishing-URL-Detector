import os
import pyfiglet
import requests
from termcolor import colored
from tldextract import tldextract
from whiteBlacklist import WhiteBlackApp
from sklearn.externals import joblib


classifier = joblib.load('final_models/rf_final.pkl')

class checkURL:

    def __init__(self, url):
        self.url = url
        self.domain = ""
        self.id = ""
        self.show_banner()

    def extract_domain(self):
        self.domain = tldextract.extract(self.url).domain

    def get_url(self):
        if not self.url.startswith("http"):
            self.url = "http://" + self.url

        head = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
        try:
            request = requests.get(self.url, headers=head)
            self.url = request.url

        except Exception as e:

            os.system("clear")
            self.show_banner()
            print("URL: " + self.url)
            print("AN ERROR OCCURRED. THE URL MIGHT NOT BE VALID OR LIVE")
            exit()

    def run(self):
        self.get_url()
        print("URL: " + self.url)

        self.extract_domain()
        white_black_test = WhiteBlackApp(self.url, self.domain)
        white_black_results = white_black_test.run()

        if white_black_results[0]:
            print("THE URL HAS BEEN DETERMINED AS PHISHY")
        elif white_black_results[1]:
            print("THE URL HAS BEEN DETERMINED AS NOT PHISHY")
        else:
            prediction = classifier.predict(checkprediction)
            if (prediction == 1):
                print("THE URL HAS BEEN DETERMINED AS PHISHY VIA MACHINE LEARNING")
            else:
                print("THE URL HAS BEEN DETERMINED AS NOT PHISHY VIA MACHINE LEARNING")
        exit()
