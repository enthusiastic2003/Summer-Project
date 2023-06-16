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
            # time.sleep(5)
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

#page for displaying insightsI
@app.route("/insights1")
def insightsI():
    #column names
    cols = list(df.columns)
    
    # Row 1:- no. of missing values
    misses = df.isnull().sum()
    
    # Row 2:- no. of present values
    present = list(df.count())
    
    # Row 3:- type of data
    dtypes = list(df.dtypes.astype("str"))
    
    # Row 4:- no. of unique values
    unique = list(df.nunique())
    
    row1 = pd.DataFrame([present], columns=cols)
    row2 = pd.DataFrame([misses], columns=cols)
    row3 = pd.DataFrame([dtypes], columns=cols)
    row4 = pd.DataFrame([unique], columns=cols)
   
    df_req = pd.concat([row1, row2, row3,row4], keys = ["Counts","Missing Values","Type","Unique Values"])
    df_req = df_req.droplevel(1)
    return render_template("/fundamentals/insightsI.html", dataset = df_req.to_html())
   
#page for displaying insights2
@app.route("/insights2")
def insightsII():
    cols = list(df.columns)
    
    # Row 1:- minimum values
    rep = "NC"
    min_val = list(df.min())
    min_val = [rep if type(x) == "str" else x for x in min_val]

    # Row 2:- maximum values
    max_val = list(df.max())
    max_val = [rep if type(x) == "str" else x for x in max_val]

    # Calculation for further steps
    df_copy = df
    array = []
    a = list(df.dtypes.astype("str"))
    c = list(df.columns)
    for i in range(len(a)):
        if a[i] == "object":
            change = c[i]
            array.append(i)
            df_copy[change] = -1

    # Row 3:- Difference in min and max values
    diff = df.max() - df.min()

    # Row 4:- Mean of the values
    mean = df_copy.mean()

    # Row 5:- Median of the values
    median = df_copy.median()

    # Row 6:- Mean/Median difference
    diff2 = abs(df.median() - df.mean())

    # Row 7:- Standard Deviation of the values
    std = df_copy.std()

    row1 = pd.DataFrame([min_val], columns=cols)
    row2 = pd.DataFrame([max_val], columns=cols)
    row3 = pd.DataFrame([diff], columns=cols)
    row4 = pd.DataFrame([mean], columns=cols)
    row5 = pd.DataFrame([median], columns=cols)
    row6 = pd.DataFrame([diff2], columns=cols)
    row7 = pd.DataFrame([std], columns=cols)

    df_req = pd.concat([row1, row2, row3,row4, row5, row6, row7], keys = ["Minimum","Maximum","Difference","Mean","Median","Mean-Median Difference","Standard Deviation"])
    df_req = df_req.droplevel(1)

    for i in range(len(array)):
        index = array[i]
        change = c[index]
        df_req[change] = "NC"
    
    return render_template("/fundamentals/insightsII.html", dataset = df_req.to_html())
    
if __name__=="__main__":
    app.run(host="0.0.0.0")
