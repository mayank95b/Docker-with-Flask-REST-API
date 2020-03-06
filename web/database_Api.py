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
db = client.sentencesDatabase
Users = db["Users"]

class Register(Resource):
    def post(self):
        #Step1 : Get posted data by Users
        postedData = request.get_json()

        #Get the data
        username = postedData["username"]
        password = postedData["password"]#123xtz

        #hash(password + salt) - wdsfdfglglkkrkglggmdlfl
        hashed_pw = bcrypt.hashpw(password, bcrypt.gensalt())

        #Store username and pw into the database
        users.insert({
        "Username": username,
        "Password": hashed_pw,
        "Sentence": "",
        "Tokens" : 5
        })

        retJson = {
           "status": 200,
           "msg" : "You successfully signed up for the API"
        }
        return jsonify(retJson)

  class Store(Resource):
      def post(self):
          #Step1 : Get posted data by Users
          postedData = request.get_json()

          #Step2 : Read the data
          username = postedData["username"]
          password = postedData["password"]
          sentence = postedData["sentence"]

          #Step3 : Verify the username pw  match
          correct_pw = verifyPw(username, password)

          if not correct_pw:
              retJson = {
                  "status":302
              }
              return jsonify(retJson)
          #Step4 : Verify user has enough Tokens
          enough_tokens = verifyTokens(username)
          if not enough_tokens:
              retJson = {
                  "status": 301
              }
              return jsonify(retJson)

          #Step5 : store the sentence, take one token away and return 2000k
          users.update({
              "Username":username
          }, {
               "$set":{
                  "Sentence":sentence,
                  "Tokens":num_tokens-1
               }

          })
  api.add_resource(Register, '/register')


UserNum.insert({
    'num_of_users':0
})

class  Visit(Resource):
    def get(self):
        prev_num = UserNum.find({})[0]['num_of_users']
        new_num = prev_num + 1
        UserNum.update({}, {"$set":{"num_of_users":new_num}})
        return str("Hello user " + str(new_num))
