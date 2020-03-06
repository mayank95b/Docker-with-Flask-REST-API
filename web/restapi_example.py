'''
Registration of a user 0 tokens
Each user gets 10 tokens
Store a sentence on our database for 1 token
Retrieve his stored sentence on out database for 1 token
'''

from flask import Flask, jsonify,request
from flask_restful import Api, Resource

from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.aNewDB
UserNum = db["UserNum"]

UserNum.insert({
    'num_of_users':0
})

class  Visit(Resource):
    def get(self):
        prev_num = UserNum.find({})[0]['num_of_users']
        new_num = prev_num + 1
        UserNum.update({}, {"$set":{"num_of_users":new_num}})
        return str("Hello user " + str(new_num))

def checkPostedData(postedData, functionName):
    if (functionName == "add") or (functionName == "Subtract") or (functionName == "Multiply"):
        if "x" not in postedData or "y" not in postedData:
            return 301
        else:
            return 200
    elif (functionName == "Divide"):
        if "x" not in postedData or "y" not in postedData:
            return 301
        elif int(postedData["y"]) == 0:
            return 302
        else :
            return 200



class Add(Resource):
    def post(self):
        # In this block, resource Add was requested using the method POST
        # Step1 : Get posted data :
        postedData = request.get_json()

        # Step1b :Verify the validity of posted data
        status_code = checkPostedData(postedData, "add")
        if (status_code !=200):
            retJson = {
            "Message": "An error have occurred",
            "Status code" : status_code
            }
            return jsonify(retJson)
        # if we are here then status code == 200
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        ret = x+y
        retMap = {
        'sum': ret,
        'Status code':200
        }
        return jsonify(retMap)
    pass

class Subtract(Resource):
    def post(self):
        # In this block, resource Add was requested using the method POST
        # Step1 : Get posted data :
        postedData = request.get_json()

        # Step1b :Verify the validity of posted data
        status_code = checkPostedData(postedData, "Subtract")
        if (status_code !=200):
            retJson = {
            "Message": "An error have occurred",
            "Status code" : status_code
            }
            return jsonify(retJson)
        # if we are here then status code == 200
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        ret = x-y
        retMap = {
        'sum': ret,
        'Status code':200
        }
        return jsonify(retMap)
    pass

class Multiply(Resource):
    def post(self):
        # In this block, resource Add was requested using the method POST
        # Step1 : Get posted data :
        postedData = request.get_json()

        # Step1b :Verify the validity of posted data
        status_code = checkPostedData(postedData, "Multiply")
        if (status_code !=200):
            retJson = {
            "Message": "An error have occurred",
            "Status code" : status_code
            }
            return jsonify(retJson)
        # if we are here then status code == 200
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        ret = x*y
        retMap = {
        'sum': ret,
        'Status code':200
        }
        return jsonify(retMap)
    pass

class Divide(Resource):
    def post(self):
        # In this block, resource Add was requested using the method POST
        # Step1 : Get posted data :
        postedData = request.get_json()

        # Step1b :Verify the validity of posted data
        status_code = checkPostedData(postedData, "Divide")
        if (status_code !=200):
            retJson = {
            "Message": "An error have occurred",
            "Status code" : status_code
            }
            return jsonify(retJson)
        # if we are here then status code == 200
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        ret = (x*1.0)/y
        retMap = {
        'sum': ret,
        'Status code':200
        }
        return jsonify(retMap)
    pass

api.add_resource(Add, "/add")
api.add_resource(Subtract, "/Subtract")
api.add_resource(Multiply, "/Multiply")
api.add_resource(Divide, "/Divide")
api.add_resource(Visit, "/Hello")



@app.route('/')
def secondpage():
    return "Welcome back"

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host='0.0.0.0')
