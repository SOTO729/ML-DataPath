from flask import Flask,request,jsonify
import requests

app=Flask(__name__)

@app.route('/helloworld',methods=['GET'])
def hello_world():
    return 'eo'