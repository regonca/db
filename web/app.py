from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import os

from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.aNewDB
UserNum = db["UserNum"]

if UserNum.count_documents({}) == 0:
    UserNum.insert_one({"num_of_users":0})

class Visit(Resource):
    def get(self):
        prevNum = UserNum.find_one({})["num_of_users"]
        newNum = prevNum + 1
        UserNum.update_one({}, {"$set":{"num_of_users":newNum}})
        return str("Hello user " + str(newNum))


def checkPostedData(postedData, functionName):
    if (functionName=="add" or functionName=="substract" or functionName=="multiply"):
        if "x" not in postedData or "y" not in postedData:
            return 301  # missing parameters
        else:
            return 200  # ok
    elif (functionName=="divide"):
        if "x" not in postedData or "y" not in postedData:
            return 301
        elif int(postedData["y"])==0:
            return 302
        return 200
    else:
        return 200

class Add(Resource):
    def post(self):
        #If I am here, them the resource Add was requested using the method POST
        pass

        # Step1: Get posted data
        postedData = request.get_json()

        # Step1b: Verify validity of postedData
        status_code = checkPostedData(postedData, "add")
        if (status_code!=200):
            retJson={
                "Message":"An error happened. Missing parameters.",
                "Status Code":status_code
            }
            return jsonify(retJson)

        # if I am here, them the status code is 200
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)

        #Step 2: Add posted data
        ret = x+y
        retMap = {
            'Message':ret,
            'Status code': 200
        }
        
        #Step 3: 
        return jsonify(retMap)


"""
    def get(self):
        #If I am here, them the resource Add was requested using the method GET
        pass
    def put(self):
        pass
    def delete(self):
        pass
"""

class Substract(Resource):
    def post(self):
        #If I am here, them the resource Substract was requested using the method POST
        pass

        # Step1: Get posted data
        postedData = request.get_json()

        # Step1b: Verify validity of postedData
        status_code = checkPostedData(postedData, "substract")
        if (status_code!=200):
            retJson={
                "Message":"An error happened. Missing parameters.",
                "Status Code":status_code
            }
            return jsonify(retJson)

        # if I am here, them the status code is 200
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)

        #Step 2: Substract posted data
        ret = x-y
        retMap = {
            'Message':ret,
            'Status code': 200
        }
        
        #Step 3: 
        return jsonify(retMap)

class Multiply(Resource):
    def post(self):
        #If I am here, them the resource Multiply was requested using the method POST
        pass

        # Step1: Get posted data
        postedData = request.get_json()

        # Step1b: Verify validity of postedData
        status_code = checkPostedData(postedData, "multiply")
        if (status_code!=200):
            retJson={
                "Message":"An error happened. Missing parameters.",
                "Status Code":status_code
            }
            return jsonify(retJson)

        # if I am here, them the status code is 200
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)

        #Step 2: Multiply posted data
        ret = x*y
        retMap = {
            'Message':ret,
            'Status code': 200
        }
        
        #Step 3: 
        return jsonify(retMap)
    
class Divide(Resource):
    def post(self):
        #If I am here, them the resource Divide was requested using the method POST
        pass

        # Step1: Get posted data
        postedData = request.get_json()

        # Step1b: Verify validity of postedData
        status_code = checkPostedData(postedData, "divide")
        if (status_code!=200):
            retJson={
                "Message":"An error happened. Missing parameters.",
                "Status Code":status_code
            }
            return jsonify(retJson)

        # if I am here, them the status code is 200
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)

        """
        # Check for Division by Zero
        if (y==0):
            retJson = {
                "Message":"Division by Zero. The second number must be greater than Zero!",
                "Status Code":302
            }
            return jsonify(retJson)
        """
            
        #Step 2: Divide posted data
        ret = (x*1.0)/y
        retMap = {
            'Message':ret,
            'Status code': 200
        }
        
        #Step 3: 
        return jsonify(retMap)


api.add_resource(Add, "/add")
api.add_resource(Substract, "/substract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Divide, "/divide")
api.add_resource(Visit, "/hello")

@app.route('/')
def hello_world():
    return "Hello_world"

if __name__== "__main__":
    app.run(host='0.0.0.0')

