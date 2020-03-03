from flask import Flask #Flask is the constructor of flask application
from flask import jsonify,request
app = Flask(__name__) #__name__ can be any title name

@app.route('/add_two_num', methods = ['POST'])
def add_two_num():
    # Get x,y from the posted send_data
    dataDict = request.get_json()

    if "y" not in dataDict:
        return "ERROR", 305
    x = dataDict["x"]
    y = dataDict["y"]

    # Add z =x+y
    z = x + y

    # Prepare a JSON, "z":z
    retJSON = {
     "z":z
     }

    # Return jsonify(map_prepared)
    return jsonify(retJSON)


if __name__ == "__main__":
    # app.run(host="127.0.0.1", port=5000)
    app.run(debug=True )
