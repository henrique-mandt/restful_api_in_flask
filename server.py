from flask import Flask, Response, request
import pymongo
import json

app = Flask(__name__)

try:
    mongo = pymongo.MongoClient(
        host="localhost", 
        port=27017,
        serverSelectionTimeoutMS = 1000)
    db = mongo.mandt    
    mongo.server_info() # trigger exception if cannot connect to db
except:
    print("ERROR - Cannot connect to db")

###########################
@app.route("/users", methods=['POST'])
def create_user():
    try:
        user = {"name": request.form["name"], 
        "lastName": request.form["lastName"]}
        dbResponse = db.users.insert_one(user)
        # for attribute in dir(dbResponse):
        #    print(attribute)
        return Response(
            response=json.dumps(
                {"message": "user created",
                "id": f"{dbResponse.inserted_id}"}),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        print(ex)


###########################
if __name__ == "__main__":
    app.run(port=6393, debug=True)