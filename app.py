import csv
from flask import Flask, render_template, request

# data_dir = "Malicious URLs.csv"
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import random
# import re

# # %matplotlib inline

# # Import Scikit-learn helper functions
# from sklearn.model_selection import train_test_split
# from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

# # Import Scikit-learn models
# from sklearn.linear_model import LogisticRegression
# from sklearn.naive_bayes import MultinomialNB

# # Import Scikit-learn metric functions
# from sklearn.metrics import confusion_matrix, classification_report
# import seaborn as sns

# print("\n### Libraries Imported ###\n")

# """# Load the dataset
# With this set, we first need to load our CSV data.
# """

# # Load the training data
# print("- Loading CSV Data -")
# _df = pd.read_csv(data_dir)

# test_ = _df['URLs'][4]

# print("\n### CSV Data Loaded ###\n")

# print(_df)

app = Flask(__name__)


# @index.route('/')
# def index1():
#     return render_template('getInput.html')


@app.route('/', methods=['GET','POST'])
def getvalue():
    if request.method == "POST":
        URL = request.form.get("URL")
        with open('dataset2.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['URL'] == URL and row['Target'] == "no":
                    output = "This is a Valid website"
                    break
                elif row['URL'] == URL and row['Target'] == "yes":
                    output = "This is an inValid website"
                    break
            else:
                output = "Not recognised"

        return render_template("getInput.html", value = output)
    return render_template("getInput.html")



#  URL = input("Please provide : ")
# #  = getvalue()
# with open('Malicious s.csv') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         if row['s'] == URL  and row['Class'] == "good":
#             output = "This is a Valid website"
#             break
#         elif row['s'] == URL and row['Class'] == "bad":
#             output = "This is an inValid website"
#             break
#     else:
#         output = "Not recognised"
#
#     print(output)

# df = pd.read_csv(data_dir, usecols = ['s'])
# print(df)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
