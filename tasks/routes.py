from flask import Blueprint, render_template, request, redirect, url_for
from bson.objectid import ObjectId
from pymongo import MongoClient
import os
import json

tasks_bp = Blueprint('tasks_bp', __name__)

client = MongoClient(os.getenv("URL"))
mongo = client['team_management']
users = mongo['Users']
projects = mongo['Projects']
tasks = mongo['Tasks']

@tasks_bp.route("/get_tasks")
def get_tasks():    
    task_list = tasks.find()
    return render_template("tasks/get_tasks.html", task_list=task_list)

@tasks_bp.route("/add_task", methods=["POST","GET"])
def add_task():
    if request.method == "POST":
        
        new_task = {
            'Name': request.form['name'],
            'Description': request.form['description'],
            'User': request.form['user'],
            'Project': request.form['project']
        }
        
        task_id = tasks.insert_one(new_task).inserted_id
        users.update_one({"_id":ObjectId(new_task['User'])},{"$addToSet":{"Tasks":ObjectId(task_id)}})
        projects.update_one({"_id":ObjectId(new_task['Project'])}, {"$addToSet":{"Tasks":ObjectId(task_id)}})
        
        return redirect(url_for('tasks_bp.get_tasks'))
    
    user_list = list(users.find())
    project_list = list(projects.find())
    return render_template("tasks/add_task.html", user_list=user_list, project_list=project_list)        

@tasks_bp.route("/task_detail/<task_id>")
def task_detail(task_id):
    task = tasks.find_one({"_id":ObjectId(task_id)})
    user = users.find_one({"Tasks": {"$elemMatch": {"$eq": ObjectId(task_id)}}})
    project = projects.find_one({"Tasks": {"$elemMatch": {"$eq": ObjectId(task_id)}}})
    return render_template("tasks/task_details.html", task=task, user=user, project=project)

@tasks_bp.route("/task_edit/<task_id>", methods=["POST", "GET"])
def task_edit(task_id):
    task = tasks.find_one({"_id": ObjectId(task_id)})
    
    if request.method == "POST":
        new_task = {
            'Name': request.form['name'],
            'Description': request.form['description'],
        }
        
        comments_json = request.form.get('comments-json')
        if comments_json:
            try:
                comments = json.loads(comments_json)
                if isinstance(comments, list):
                    new_task['Comments'] = comments
            except json.JSONDecodeError:
                print("Error decoding JSON from comments-json")
        
        tasks.update_one({"_id": ObjectId(task_id)}, {"$set": new_task})
        return redirect(url_for('tasks_bp.get_tasks'))
    
    return render_template("tasks/edit_task.html", task=task)

@tasks_bp.route("/task/delete_task/<task_id>", methods=["POST"])
def delete_task(task_id):
    tasks.delete_one({"_id":ObjectId(task_id)})
    return redirect(url_for('tasks_bp.get_tasks'))
