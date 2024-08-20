from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from bson.objectid import ObjectId

# App and db configuration
app = Flask(__name__)
client = MongoClient(os.getenv("URL"))
mongo = client['team_management']

# Collection
users = mongo['Users']

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_users")
def get_users():
    users_list = list(users.find())
    return render_template("get_users.html", users_list=users_list)

@app.route("/add_user")
def add_user():
    return render_template("add_user.html")

@app.route("/user_details/<user_id>")
def user_details(user_id):
    user = users.find_one({"_id": ObjectId(user_id)})
    return render_template("user_details.html", user=user)

@app.route("/edit_user/<user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    user = users.find_one({"_id":ObjectId(user_id)})
    if request.method == "POST":
        updated_user = {
            'Name': request.form['name'],
            'Email': request.form['email'],
            'Role': request.form['role']
        }
        
        users.update_one({"_id": ObjectId(user_id)}, {"$set":updated_user})
        return render_template("user_details.html", user=user)
    return render_template("edit_user.html", user=user)

@app.route("/delete_user/<user_id>")
def delete_user(user_id):
    users.delete_one({"_id":ObjectId(user_id)})
    return render_template("get_users.html")

