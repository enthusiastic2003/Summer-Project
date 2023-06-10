from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import time
app = Flask(__name__ )


#home page
@app.route("/")
def home():
    return render_template("index.html")

#first page for uploading the dataset
@app.route("/page1")
def page1():
    return render_template("firstpage.html")

#uploading the dataset
@app.route("/upload", methods = ["POST"])
def upload():
    global df
    if request.method == "POST":
        file = request.files["file"]
        if file:
            df = pd.read_csv(file)
            time.sleep(5)
            return render_template("uploadsuccess.html", message = "Dataset Uploaded Successfully")
        else:
            return render_template("firstpage.html", message = "Dataset not uploaded")
        
#main intro page
@app.route("/main")
def main():
    return render_template("main.html") 

# main page with features
@app.route("/main_1")
def main_1():
    return render_template("main_1.html")       

#page for displaying the dataset
@app.route("/dset")
def page2():
    if df is not None:
        return render_template("dataset.html", dataset = df.to_html())
    else:
        return render_template("dataset.html", dataset = "Dataset not uploaded")

# #This will display size of uploaded dataset
# @app.route("/shape")
# def shape():
#     global rc
#     rc = df.shape
#     rows = rc[0]
#     columns = rc[1]
#     rc = f"Rows: {rows} Columns: {columns}"
#     return render_template("main_1.html",shape = rc)

# #This will display the missing values in the dataset
# @app.route("/miss")
# def miss():
#     global miss_values
#     values = list(df.isnull().sum())
#     miss_values = []
#     arr = list(df.columns)
#     for i in range(len(values)):
#         if values[i] != 0:
#             miss_values.append((arr[i], values[i])) # to get a list of tuples of feature and number of missing values
        
#     return render_template("main_1.html", missing_values = miss_values, shape = rc)


if __name__=="__main__":
    app.run(host="0.0.0.0")
