# Task Manager API

A Django REST API for managing personal tasks with user authentication and token-based security.

## Features

- 👤 **User Registration & Authentication** - Secure user registration and login via token-based authentication
- 📋 **Task Management** - Create, read, update, and delete personal tasks
- 🔐 **Task Ownership** - Tasks are tied to specific users with no cross-user access
- 📊 **Task Status Tracking** - Mark tasks as completed/incomplete with timestamps
- 🔄 **RESTful API** - Modern API endpoints following REST principles
- 🛡️ **Security** - Password protection, user isolation, and token authentication

## Tech Stack

- **Django 5.1.2** - Main web framework
- **Django REST Framework 3.17.0** - API development framework
- **SQLite** - Database (no external setup required)
- **Token Authentication** - Built-in Django REST Framework auth
- **Python 3.x** - Programming language

## Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd task_manager
   ```

2. **Create and activate virtual environment**
   ```bash
   # On Windows
   python -m venv env
   env\Scripts\activate
   
   # On macOS/Linux
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://127.0.0.1:8000/`

## API Endpoints

### Authentication

- `POST /api/auth/register/` - Register new user
- `POST /api/auth/login/` - Login and get authentication token

### Task Management

- `GET /api/tasks/` - List all tasks for authenticated user
- `POST /api/tasks/` - Create new task
- `GET /api/tasks/<id>/` - Get task details
- `PUT /api/tasks/<id>/` - Update task
- `DELETE /api/tasks/<id>/` - Delete task

## Usage Examples

### Register a new user
```bash
curl -X POST http://127.0.0.1:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpass", "email": "test@example.com"}'
```

### Login and get token
```bash
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpass"}'
```

### Create a new task (with token)
```bash
curl -X POST http://127.0.0.1:8000/api/tasks/ \
  -H "Authorization: Token your_auth_token" \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy groceries", "description": "Milk, eggs, bread"}'
```

## Project Structure

```
task_manager/
├── task_manager/          # Django project configuration
│   ├── settings.py        # Project settings
│   ├── urls.py           # Root URL routing
│   └── wsgi.py           # WSGI configuration
├── tasks/                # Main application
│   ├── models.py         # Task and User models
│   ├── serializers.py    # API serializers
│   ├── views.py          # API views
│   ├── urls.py          # App URL routing
│   └── admin.py         # Admin configuration
├── env/                 # Virtual environment
└── manage.py           # Django management command
```

## Security Features

- **Password Protection**: Passwords are write-only and never returned in API responses
- **User Isolation**: Users can only access their own tasks
- **Token Authentication**: Secure API access without session cookies
- **CSRF Protection**: Built-in Django security features

## Development

### Running Tests
```bash
python manage.py test
```

### Code Quality
```bash
# Run linting (if configured)
python manage.py check

# Type checking (if configured)
python manage.py check --settings=task_manager.settings
```

## Deployment

For production deployment:
1. Set `DEBUG = False` in settings.py
2. Configure a production-ready database (PostgreSQL, MySQL, etc.)
3. Set up a web server (Nginx/Apache) with WSGI
4. Configure HTTPS and security headers
5. Set up proper logging and monitoring

## License

This project is licensed under the MIT License.

## Support

For support and questions:
- Create an issue in the repository
- Check the Django REST Framework documentation
- Review Django security best practices