import json 
import requests 
from flask import Flask,render_template,request,jsonify 

app = Flask(__name__)

@app.route("/")
def index():

     return render_template("get_ip.html")
if __name__=="__main__":

            app.run(debug=True,threaded=True,host="0.0.0.0",port=9020)
