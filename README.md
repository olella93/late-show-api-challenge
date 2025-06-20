 ### Late Show API

 A RESTful API for managing guests, episodes, and appearances on a fictional late-night talk show. Built with Flask, PostgreSQL, and JWT authentication.

 ### Tech Stack

 - Backend: Flask

- ORM: SQLAlchemy

- Database: PostgreSQL

- Auth: JWT (via flask-jwt-extended)

- Migrations: Flask-Migrate

- Testing Tool: Postman

### Project Structure (MVC)

late-show-api-challenge/
│
├── server/
│   ├── app.py
│   ├── config.py
│   ├── extensions.py
│   ├── seed.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── guest.py
│   │   ├── episode.py
│   │   └── appearance.py
│   └── controllers/
│       ├── auth_controller.py
│       ├── guest_controller.py
│       ├── episode_controller.py
│       └── appearance_controller.py
│
├── migrations/
├── .venv/
└── README.md

### Authentication

- POST /auth/register: Register and receive JWT

- POST /auth/login: Log in and receive JWT

Use the token in Authorization: Bearer <your_token> header to access protected routes.

### API Routes

| Route            | Method | Auth | Description                         |
| ---------------- | ------ | ---- | ----------------------------------- |
| `/auth/register` | POST   | ❌    | Register a new user                 |
| `/auth/login`    | POST   | ❌    | Login and receive a token           |
| `/episodes`      | GET    | ❌    | List all episodes                   |
| `/episodes/<id>` | GET    | ❌    | Get episode with appearances        |
| `/episodes/<id>` | DELETE | ✅    | Delete episode with its appearances |
| `/guests`        | GET    | ❌    | List all guests                     |
| `/appearances`   | POST   | ✅    | Create a new appearance             |

### Seeding

Run the following command to seed the database:

PYTHONPATH=. python server/seed.py

###  Setup Instructions

1. ## Clone Repo & Set Up Virtual Environment

git clone <your-repo-url>
cd late-show-api-challenge
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

2. ## Set Environment Variables

export FLASK_APP=server/app.py
export FLASK_ENV=development
export PYTHONPATH=.

3. ## Initialize DB

flask db init
flask db migrate -m "Initial migration"
flask db upgrade

4. ## Run the App

flask run

### Author
Richard Olella 

GitHub Repo Link: https://github.com/olella93/late-show-api-challenge