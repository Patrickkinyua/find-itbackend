# Find-It Backend

A robust backend for the Find-It application, designed to help users report and recover lost items. Built with Django and Django REST Framework.

## Features

### Authentication & Users
- **Custom User Model**: Email-based authentication (no username required).
- **JWT Authentication**: Secure stateless authentication using `simplejwt`.
- **User Profiles**: Extended user details including bio, location, and notification preferences.
- **Profile Management**: Endpoints for registration, login, profile updates, password change, and avatar upload.

### Lost & Found Items
- **Report Lost Items**: Users can post details about lost items including images, location, and category.
- **Report Found Items**: Users can report found items to help others recover them.
- **Categorization**: Items are organized by categories (e.g., Electronics, Keys, Wallets).
- **Search & Filter**: Advanced search capabilities by title, description, location, and category.
- **Image Handling**: Support for multiple images per item.

## Tech Stack

- **Framework**: Django 5.2.8
- **API**: Django REST Framework
- **Database**: SQLite (Default)
- **Authentication**: JWT (JSON Web Tokens)
- **Language**: Python 3.13

## Setup Instructions

### Prerequisites
- Python 3.13+
- Pipenv (recommended) or pip

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd find-itbackend
   ```

2. **Install Dependencies**
   Using Pipenv:
   ```bash
   pipenv install
   pipenv shell
   ```
   Or using pip:
   ```bash
   pip install -r requirements.txt  # If requirements.txt exists
   # OR manually install packages listed in Pipfile
   pip install django djangorestframework psycopg2-binary python-dotenv djangorestframework-simplejwt pillow
   ```

3. **Apply Migrations**
   ```bash
   python manage.py migrate
   ```

4. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Authentication (`/api/auth/`)
- `POST /register/`: Register a new user.
- `POST /login/`: Login and obtain JWT tokens.
- `POST /token/refresh/`: Refresh access token.
- `POST /logout/`: Logout (blacklist refresh token).
- `POST /password/change/`: Change user password.
- `GET/PUT /profile/`: Get or update user profile.

### Items (`/api/`)
- `GET/POST /lost-items/`: List or create lost item reports.
- `GET/POST /found-items/`: List or create found item reports.
- `GET/POST /categories/`: Manage item categories.
- `POST /item-images/`: Upload images for items.
