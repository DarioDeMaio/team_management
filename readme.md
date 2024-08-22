# Team Project Management App

## Description

This is a simple web application designed for managing team projects and tasks. The application allows users to create projects, assign tasks to team members, track project progress, add comments to specific tasks, and manage deadlines with a calendar view.

## Features

- **User Management**: Create and manage users with different roles (e.g., developer, project manager).
- **Project Management**: Create, update, and delete projects. Assign multiple users to a project.
- **Task Assignment**: Create and assign tasks to specific team members within a project. Each task includes a description, status, due date, and assigned user.
- **Task Comments**: Add, view, and manage comments on specific tasks for collaboration and updates.
- **Project Progress**: Track the status of ongoing projects and view all related tasks.
- **Calendar**: Visualize task deadlines and project timelines on a calendar.

## Database Structure

The application uses MongoDB to store data, organized into the following collections:

1. **Users**
    - Stores user details including name, email, role, and associated projects.
    
2. **Projects**
    - Stores project details including name, description, assigned members, and related tasks.
    
3. **Tasks**
    - Stores task details including name, description, status, assigned user, date, and comments.

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

1. **Register** as a new user or **log in** with an existing account.
2. Create a new project and assign team members.
3. Add tasks to the project and assign them to specific members.
4. Track the progress of tasks and projects.
5. Add comments to tasks for better communication.
6. Use the calendar view to manage deadlines.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
