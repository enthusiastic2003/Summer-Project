from flask import Flask, render_template, request, g
import pandas as pd
import numpy as np
app = Flask(__name__ )

#declaring the global variable for dataset
@app.before_request
def before_request():
    g.dataset = None;

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
    if request.method == "POST":
        file = request.files["file"]
        if file:
            g.dataset = pd.read_csv(file)
            return render_template("firstpage.html", message = "Dataset uploaded successfully")
        else:
            return render_template("firstpage.html", message = "Dataset not uploaded")
        
        

if __name__=="__main__":
    app.run(host="0.0.0.0")
