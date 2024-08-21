from flask import Blueprint, render_template, request, redirect, url_for
from bson.objectid import ObjectId
from pymongo import MongoClient
import os

# Create the blueprint for users
projects_bp = Blueprint('projects_bp', __name__)

client = MongoClient(os.getenv("URL"))
mongo = client['team_management']
users = mongo['Users']
projects = mongo['Projects']

# Route definitions for projects
@projects_bp.route("/get_projects")
def get_projects():
    projects_list = list(projects.find())
    return render_template("projects/get_projects.html", projects_list=projects_list)

@projects_bp.route("/add_projects", methods=["GET", "POST"])
def add_projects():
    if request.method == "POST":
        new_project = {
            'Name': request.form['name'],
            'Description': request.form['description'],
            'Members': request.form.getlist('members')
        }
        
        id_project = projects.insert_one(new_project).inserted_id
        
        for member in request.form.getlist('members'):
            new_user = users.find_one({"_id": ObjectId(member)})
            if 'Projects' in new_user and new_user['Projects']:
                new_user['Projects'].append(ObjectId(id_project))
            else:
                new_user['Projects'] = [ObjectId(id_project)]
            
            users.update_one({"_id": ObjectId(member)}, {"$set": {"Projects": new_user['Projects']}})
        
        return redirect(url_for('projects_bp.get_projects'))
    
    user_list = list(users.find())
    return render_template("projects/add_project.html", user_list=user_list)
