

# Yet Another Tweeter Basic Clone

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Installation Guide](#installation-guide)
5. [Project Structure](#project-structure)
6. [Running the Project](#running-the-project)
7. [Database Migrations](#database-migrations)
8. [Contributing](#contributing)
9. [Known Issues](#known-issues)
10. [License](#license)

## Project Overview
**Yet Another Tweeter Basic Clone** is a simple Twitter-like web app built using Django. It allows users to tweet, interact with posts, and manage profiles. This project emphasizes Django Forms and fundamental web technologies.

## Features
- User authentication (login, registration).
- Posting tweets (text limit of 240 characters).
- Dynamic tweet feed.
- Basic profile management.

## Tech Stack
- **Backend**: Django 4.x
- **Frontend**: HTML, CSS (Tailwind CSS for styling), JavaScript
- **Database**: SQLite (default for Django)
- **Version Control**: Git, GitHub

## Installation Guide
1. **Clone the repository**:
   ```bash
   git clone https://github.com/itsjazzkun/Yet-Another-Tweeter-Basic-Clone.git
   cd Yet-Another-Tweeter-Basic-Clone
   ```
2. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```

## Project Structure
```
Yet-Another-Tweeter-Basic-Clone/
├── YABTC/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tweet/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
├── manage.py
└── requirements.txt
```

## Running the Project
Start the Django development server:
```bash
python manage.py runserver
```
Visit the app at `http://127.0.0.1:8000/`.

## Database Migrations
To create and apply migrations for your models:
```bash
python manage.py makemigrations
python manage.py migrate
```

## Contributing
Feel free to fork the project, submit pull requests, or report issues. Contributions are always welcome!

## Known Issues
 
- When attempting to delete a tweet, a prompt should ask for confirmation: "Are you sure you want to delete this tweet?"

- User authentication is not implemented yet.

## License
This project is licensed under the MIT License.

---
