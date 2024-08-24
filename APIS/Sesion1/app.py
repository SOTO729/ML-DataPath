from flask import Flask,request,jsonify
import requests

app=Flask(__name__)

@app.route('/helloworld',methods=['GET'])
def hello_world():
    return 'eo'

@app.route('/despedida',methods=['GET'])
def despedida():
    return 'adios'


#@app.route('/pokemon',methods=['GET'])
#def hello_world():
#    url=
#    return 'eo'