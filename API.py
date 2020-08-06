from flask import Flask,request ,jsonify
import ContentBased as co
import requests, json
import Apriori as AP
import Collaborativefiltering as CF
import pandas as pd
import jwt

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/",methods=['GET','POST'])
def apriori():
    print("success!!!")
    return AP.Apriori()

@app.route("/content",methods=['POST','GET'])
def content():
    req = request.get_json()
    data = req
    print(data)
    if request.method == 'GET':
        return co.ContentBased(data)
    if request.method == 'POST':
        print(request.json)
    return co.ContentBased(data)



@app.route('/list/', methods=['GET','POST'])
def get_tasks():
    if request.method == 'GET':
        return jsonify(CF.similar_place)
    if request.method == 'POST':
        print(request.json)
        IPs2 = request.json
        for i in IPs2:
            if i not in CF.similar_place:
                CF.similar_place.append(i)

    print()

    return 'OK', 201
if __name__ == '__main__':
    app.run(host='192.168.43.70',port='443')
