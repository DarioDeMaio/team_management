from flask import Blueprint, render_template, request, redirect, url_for
from bson.objectid import ObjectId
from pymongo import MongoClient
import os

projects_bp = Blueprint('projects_bp', __name__)

client = MongoClient(os.getenv("URL"))
mongo = client['team_management']
users = mongo['Users']
projects = mongo['Projects']
tasks = mongo['Tasks']

@projects_bp.route("/get_projects")
def get_projects():
    projects_list = list(projects.find())
    return render_template("projects/get_projects.html", projects_list=projects_list)

@projects_bp.route("/add_projects", methods=["GET", "POST"])
def add_projects():
    if request.method == "POST":
        member_ids = [ObjectId(member_id) for member_id in request.form.getlist('members')]
        
        new_project = {
            'Name': request.form['name'],
            'Description': request.form['description'],
            'Members': member_ids
        }
        
        project_id = projects.insert_one(new_project).inserted_id
        
        for member_id in member_ids:
            user = users.find_one({"_id": member_id})
            if user:
                if 'Projects' in user:
                    user['Projects'].append(ObjectId(project_id))
                else:
                    user['Projects'] = [ObjectId(project_id)]
                users.update_one({"_id": member_id}, {"$set": {"Projects": user['Projects']}})
        
        return redirect(url_for('projects_bp.get_projects'))
    
    user_list = list(users.find())
    return render_template("projects/add_project.html", user_list=user_list)

@projects_bp.route("/project_details/<project_id>")
def project_details(project_id):
    project = projects.find_one({"_id": ObjectId(project_id)})
    
    user_ids = [ObjectId(user_id) for user_id in project.get('Members', [])]
    users_list = list(users.find({"_id": {"$in": user_ids}}))

    return render_template("projects/project_detail.html", project=project, user_list=users_list)

@projects_bp.route("/edit_project/<project_id>", methods=["GET", "POST"])
def edit_project(project_id):
    project = projects.find_one({"_id": ObjectId(project_id)})
    
    if request.method == "POST":
        updated_members = [ObjectId(member_id) for member_id in request.form.getlist('members')]
        updated_project = {
            'Name': request.form['name'],
            'Description': request.form['description'],
            'Members': updated_members
        }
        
        projects.update_one({"_id": ObjectId(project_id)}, {"$set": updated_project})
        
        for member_id in updated_members:
            user = users.find_one({"_id": member_id})
            if user:
                if 'Projects' not in user:
                    user['Projects'] = []
                if ObjectId(project_id) not in user['Projects']:
                    user['Projects'].append(ObjectId(project_id))
                users.update_one({"_id": member_id}, {"$set": {"Projects": user['Projects']}})
        
        current_members = set(ObjectId(member_id) for member_id in project.get('Members', []))
        updated_members_set = set(updated_members)
        
        for member_id in current_members - updated_members_set:
            result = users.update_one(
                {"_id": member_id},
                {"$pull": {"Projects": ObjectId(project_id)}}
            )
        
        return redirect(url_for('projects_bp.get_projects'))
    
    user_list = list(users.find())
    project = projects.find_one({"_id": ObjectId(project_id)})
    return render_template("projects/edit_project.html", project=project, user_list=user_list)


@projects_bp.route("/delete_project/<project_id>", methods=["POST"])
def delete_project(project_id):
    projects.delete_one({"_id":ObjectId(project_id)})
    return redirect(url_for('projects_bp.get_projects'))