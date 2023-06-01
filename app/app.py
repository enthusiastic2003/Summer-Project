from flask import Flask, render_template, request, g, redirect, url_for, session
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
            return redirect(url_for("page2")) 
        else:
            return render_template("firstpage.html", message = "Dataset not uploaded")
        
#second page for displaying the dataset
@app.route("/page2")
def page2():
    if df is not None:
        return render_template("secondpage.html", dataset = df.to_html())
    else:
        return render_template("secondpage.html", dataset = "Dataset not uploaded")
    
if __name__=="__main__":
    app.run(host="0.0.0.0")
