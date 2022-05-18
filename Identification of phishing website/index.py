import csv
from flask import Flask, render_template, request

data_dir = "Malicious URLs.csv"
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import re

# %matplotlib inline

# Import Scikit-learn helper functions
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

# Import Scikit-learn models
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB

# Import Scikit-learn metric functions
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns

print("\n### Libraries Imported ###\n")

"""# Load the dataset
With this set, we first need to load our CSV data.
"""

# Load the training data
print("- Loading CSV Data -")
url_df = pd.read_csv(data_dir)

test_url = url_df['URLs'][4]

print("\n### CSV Data Loaded ###\n")

print(url_df)

index = Flask(__name__)


@index.route('/')
def index1():
    return render_template('getInput.html')


@index.route('/', methods=['GET','POST'])
def getvalue():
    URL = request.form['URL']
    return URL
    # return render_template('getInput.html', URL=URL)


URL = input("Please provide URL: ")
# URL = getvalue()
with open('Malicious URLs.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['URLs'] == URL and row['Class'] == "good":
            output = "This is a Valid website"
            break
        elif row['URLs'] == URL and row['Class'] == "bad":
            output = "This is an inValid website"
            break
    else:
        output = "Not recognised"

    print(output)

# df = pd.read_csv(data_dir, usecols = ['URLs'])
# print(df)

if __name__ == '__main__':
    index.run(debug=True)
