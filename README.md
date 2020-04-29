# Phishing-URL-Detector

With the integration of Machine Learning in detecting phishing attempts, the avenue of its applications is extremely widespread. Malicious emails are a form of phishing attack, which redirects the user to visit unexpected sites or cause computer viruses to be downloaded on the user’s system. The project’s aim is to mitigate the vulnerability of such emails by using an ML algorithm to detect these URLs and notify the user of the possible danger. 

# How It Works -

Our URL Phishing detector currently scrapes the body of the last received email from your inbox, obtains the URL from it, and then using Machine Learning, it will predict whether the URL seems phishy or not. This was done by testing different ML algorithms - Logistic Regression, Support Vector Machine and Random Forest. We also came up with a list of the most important variables that determine the extent to which a URL is safe or not - some of them being - length of URL, use of HTTP or HTPPS, domain name, etc. The image of the same has been uploaded under the images section of this repository. Eventually, it turned out that Random Forest algorithm had an accuracy of roughly 97% which was the highest of all, and thus was used. Hence, now by using our URL detector, one can avoid being a victim to phishing emails or browsing potentially unsafe websites that may lead you to compromise your sensitive information such as credit card details, passwords etc, or worse, have viruses installed on your system.

# Steps to Repoduce -

# 1 
Clone the repository, and go to emailExtracter2.py and add your credentials for your imap account (you can google how to do so if unsure, may have to change certain gmail settings)
# 2 
On your terminal go to the repository, and type command: python3 -W ignore emailExtracter2.py
Now the above enabled you to save the last email to "email.txt" which you can check.
# 3 
Run the command python3 - W ignore index.py
wait for your output...you get the result!
# 4
Additionally, to check the output on a website, type python3 server.py to start the python server onto your terminal, and copy the local address onto your browser. It will show a webpage, wherein you can enter the URL to see the output. Check images folder for the webpage screenshot
