from flask import Flask #Flask is the constructor of flask application
from flask import jsonify,request
app = Flask(__name__) #__name__ can be any title name

# 127.0.0.1:5000/
@app.route('/') # means once the server i.e. app.py start running it always listening on slash(/).
def firstpage():
    return "Welcome to flask Api"

@app.route('/home')
def secondpage():
    return "Welcome to Home page"


@app.route('/data')
def send_data():
    retJson = {
     "Name" : "Mayank bhatia",  # value can be number,string,boolean & array
     "Age" : 24,
     "Designation" : "Software Engineer",
     "email" : "mayank.sde@gmail.com",
     "Phone" : [
        {
            "PhoneName": "Iphone 11",
            "phoneNumber": 11111111
        },
        {
            "PhoneName": "Redmi Note",
            "phoneNumber": 22222222
        }
     ],
     "array" : [1,2,3,4,"abc"]
    }
    return jsonify(retJson)

if __name__ == "__main__":
    # app.run(host="127.0.0.1", port=5000)
    app.run(debug=True )
