from flask import Blueprint, render_template, request, redirect, url_for
from bson.objectid import ObjectId
from pymongo import MongoClient
import os

# Create the blueprint for users
users_bp = Blueprint('users_bp', __name__)

client = MongoClient(os.getenv("URL"))
mongo = client['team_management']
users = mongo['Users']
projects = mongo['Projects']

# Route definitions for users
@users_bp.route("/get_users")
def get_users():
    users_list = list(users.find())
    return render_template("users/get_users.html", users_list=users_list)

@users_bp.route("/add_user", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        new_user = {
            'Name': request.form['name'],
            'Email': request.form['email'],
            'Role': request.form['role'],
            'Projects': request.form.getlist('projects')
        }
        users.insert_one(new_user)
        return redirect(url_for('users/users_bp.get_users'))
    all_projects = projects.find()
    return render_template("users/add_user.html", all_projects=all_projects)

@users_bp.route("/user_details/<user_id>")
def user_details(user_id):
    user = users.find_one({"_id": ObjectId(user_id)})
    return render_template("users/user_details.html", user=user)

@users_bp.route("/edit_user/<user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    user = users.find_one({"_id": ObjectId(user_id)})
    if request.method == "POST":
        selected_projects = request.form.getlist('projects')
        updated_user = {
            'Name': request.form['name'],
            'Email': request.form['email'],
            'Role': request.form['role'],
            'Projects': selected_projects
        }
        users.update_one({"_id": ObjectId(user_id)}, {"$set": updated_user})
        return redirect(url_for('users/users_bp.user_details', user_id=user_id))
    all_projects = projects.find()
    return render_template("users/edit_user.html", user=user, all_projects=all_projects)

@users_bp.route("/delete_user/<user_id>")
def delete_user(user_id):
    users.delete_one({"_id": ObjectId(user_id)})
    return redirect(url_for('users/users_bp.get_users'))
