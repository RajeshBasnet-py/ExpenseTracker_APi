# ExpenseTracker_APi


# Expense Tracker API

## Project Description

Expense Tracker API is a Django-based backend application that allows users to manage their expenses efficiently. Users can sign up, log in, and create, view, update, or delete expenses. The application supports authentication via JWT tokens to ensure secure access to user data.

This project was inspired by the roadmap on [Roadmap.sh](https://roadmap.sh/projects/expense-tracker-api), which provided the foundation for building this Expense Tracker API.

## Features

- **User Authentication**: Sign up and log in using JWT authentication.
- **Expense Management**: Add, retrieve, update, or delete expenses.
- **Expense Filtering**: Filter expenses by categories or date ranges (e.g., past week, past month, custom date).
- **Secure API**: JWT token-based authentication for secure access.

## Technologies Used

- **Django**: Web framework for building the backend.
- **Django REST Framework**: To build RESTful APIs.
- **Django SimpleJWT**: For JWT authentication.
- **SQLite**: Database for storing user and expense data (can be replaced with other databases like PostgreSQL).

## Setup Instructions

### Prerequisites

- Python 3.x
- Django 3.x or above
- Django REST Framework
- Django SimpleJWT
- SQLite or your preferred database

### Installation Steps

1. **Clone the repository**:
   ```bash
   git clone <your-repository-url>
   cd <your-project-folder>
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate     # For Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations** to set up the database:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** to access the Django admin:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the API** via:
   - `POST /api/token/` to get an access token (JWT authentication).
   - `POST /signup/` to create a new user.
   - `GET /expenses/` to list expenses (authentication required).
   - `POST /expenses/` to create a new expense (authentication required).

## API Documentation

- **POST /api/token/**: Obtain a JWT token using your username and password.
  - Request:
    ```json
    {
        "username": "your-username",
        "password": "your-password"
    }
    ```
  - Response:
    ```json
    {
        "access": "your-access-token",
        "refresh": "your-refresh-token"
    }
    ```

- **POST /signup/**: Create a new user account.
  - Request:
    ```json
    {
        "username": "new-username",
        "password": "new-password",
        "email": "user@example.com"
    }
    ```

- **GET /expenses/**: Get all expenses for the authenticated user.

- **POST /expenses/**: Create a new expense.
  - Request:
    ```json
    {
        "title": "Groceries",
        "amount": 150.75,
        "category": "Groceries",
        "date": "2025-01-08"
    }
    ```

## Roadmap

This project was inspired by the following roadmap:  
[Expense Tracker API Project Roadmap](https://roadmap.sh/projects/expense-tracker-api)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### How to upload to GitHub

1. Initialize a Git repository:
   ```bash
   git init
   ```

2. Add all files to the Git repository:
   ```bash
   git add .
   ```

3. Commit the changes:
   ```bash
   git commit -m "Initial commit of Expense Tracker API"
   ```

4. Create a new repository on GitHub (if you haven't already).

5. Add the remote repository:
   ```bash
   git remote add origin https://github.com/<your-username>/<repository-name>.git
   ```

6. Push your code to GitHub:
   ```bash
   git push -u origin master
   ```

---
