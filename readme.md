# Team Project Management App

## Description

This is a simple web application designed for managing team projects and tasks. The application allows users to create projects, assign tasks to team members and add comments to specific tasks.

## Features

- **User Management**: Create and manage users with different roles (e.g., developer, project manager).
- **Project Management**: Create, update, and delete projects. Assign multiple users to a project.
- **Task Assignment**: Create and assign tasks to specific team members within a project. Each task includes a description, status, due date, and assigned user.
- **Task Comments**: Add, view, and manage comments on specific tasks for collaboration and updates.

## Database Structure

The application uses MongoDB to store data, organized into the following collections:

1. **Users**
    - Stores user details including name, email, role, and associated projects.
    
2. **Projects**
    - Stores project details including name, description, assigned members, and related tasks.
    
3. **Tasks**
    - Stores task details including name, description, status, assigned user, date, and comments(which include a date and content).

## Technologies Used

- **Backend**: Flask (Python)
- **Database**: MongoDB
- **Frontend**: HTML, CSS, JavaScript and Bootstrap.

## Installation and Setup

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/DarioDeMaio/team_management.git
    cd team_management
    ```

2. **Create a Virtual Environment**:
    ```bash
    python3 -m venv myenv
    myenv\Scripts\activate
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up MongoDB**:
    - Ensure MongoDB is installed and running on your machine or use a cloud-based MongoDB service.
    - Update the MongoDB URI in your configuration file.

5. **Run the Application**:
    ```bash
    flask run
    ```

6. **Access the Application**:
    - Open your browser and navigate to `http://localhost:5000`.

## Usage

1. Create a new project and assign team members.
2. Add tasks to the project and assign them to specific members.
3. Add comments to tasks for better communication.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
