from flask import Flask, make_response, request, jsonify
from flask_cors import CORS,cross_origin
from flask_mongoengine import MongoEngine
from server_constants import database_name
import os 
from dotenv import load_dotenv
import re

load_dotenv()

mongodb_password = os.getenv('DB_PASS')

app = Flask(__name__)
cors = CORS(app)

DB_URI = "mongodb+srv://yoni:{}@storedb.nzje0.mongodb.net/{}?retryWrites=true&w=majority".format(
    mongodb_password, database_name)
app.config["MONGODB_HOST"] = DB_URI
app.config['CORS_HEADERS'] = 'Content-Type'

db = MongoEngine()
db.init_app(app)

class User(db.Document):
    first_name = db.StringField()
    last_name = db.StringField()
    user_id = db.StringField()

    def to_json(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "user_id": self.user_id
        }

@app.route('/api/getusers', methods=['GET'])
@cross_origin()
def get_users():
    users=User.objects.all()
    return make_response(jsonify(users), 200)

@app.route('/api/adduser', methods=['POST'])
@cross_origin()
def add_user():
    content = request.json
    if not re.match(r'^[A-Z][a-z]*$',content['first_name']):
        return make_response("First name must contain capital letter and then letters",400)
    elif not re.match(r'^[A-Z][a-z]*$',content['last_name']):
        return make_response("last name must contain capital letter and then letters",400)
    elif not re.match(r'^[0-9]+$',content['user_id']):
        return make_response("ID must contain one digit or more",400)
    else:
        user = User(first_name=content['first_name'],
                    last_name=content['last_name'],
                    user_id=content['user_id'])
        user.save()
        return make_response("User added successfully",201)

if __name__ == "__main__":
    app.run()
