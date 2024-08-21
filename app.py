from flask import Flask, render_template
from users.routes import users_bp
from projects.routes import projects_bp
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Register the blueprints
app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(projects_bp, url_prefix='/projects')

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
