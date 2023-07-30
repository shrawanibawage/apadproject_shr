from flask import Flask,  request, jsonify, render_template
from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS
from pymongo import MongoClient
import certifi
import json

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://localhost/apadproject'
mongo = PyMongo(app)
cluster = MongoClient("mongodb+srv://shrawanibawage:Shrawani7@clustertest.4curtxj.mongodb.net/" , tlsCAFile=certifi.where()) 
db = cluster.apadproject
CORS(app)
collection1 = db.users



@app.route('/login', methods=['POST'])
def check_login_details():

    data = json.loads(request.data)    
    print(data)
    result = collection1.find_one({"username":str(data["username"])})
    print(result["password"])
    if result["password"] == data["password"]:
        response = jsonify({"validLogin" : "true"})
    else:
        response = jsonify({"validLogin" : "false"})
    return response

@app.route('/register', methods=['POST'])
def register_user() :
    data = json.loads(request.data)
    if collection1.insert_one(data) :
        response = jsonify(["Registration Successful"])
    return response
    

if __name__ == "__main__":
    print("Hello")
    app.run(port=5000)
