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
    return render_template("HTML/index.html")

#first page for uploading the dataset
@app.route("/page1")
def page1():
    return render_template("HTML/firstpage.html")

if __name__=="__main__":
    app.run(host="0.0.0.0")
