# Late Show API

A RESTful API for managing guests, episodes, and appearances on a fictional late-night talk show. Built with Flask, PostgreSQL, and JWT authentication.

---

## Tech Stack

- **Backend:** Flask
- **ORM:** SQLAlchemy
- **Database:** PostgreSQL
- **Auth:** JWT (via flask-jwt-extended)
- **Migrations:** Flask-Migrate
- **Testing Tool:** Postman

---

## Project Structure (MVC)

```
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
```

---

## Setup Instructions

### 1. Install PostgreSQL

- **macOS:**  
  `brew install postgresql`
- **Ubuntu:**  
  `sudo apt-get install postgresql postgresql-contrib`

Start PostgreSQL and create a database:
```sh
createdb late_show_api_db
```

### 2. Clone Repo & Set Up Virtual Environment

```sh
git clone https://github.com/olella93/late-show-api-challenge.git
cd late-show-api-challenge
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Set Environment Variables

```sh
export FLASK_APP=server/app.py
export FLASK_ENV=development
export DATABASE_URL=postgresql://localhost/late_show_api_db
export PYTHONPATH=.
```

### 4. Initialize Database

```sh
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 5. Seed the Database

```sh
PYTHONPATH=. python server/seed.py
```

### 6. Run the App

```sh
flask run
```

---

## Authentication Flow

1. **Register:**  
   `POST /auth/register`  
   Request body:
   ```json
   {
     "username": "yourname",
     "password": "yourpassword"
   }
   ```
   Response:
   ```json
   {
     "access_token": "<JWT_TOKEN>"
   }
   ```

2. **Login:**  
   `POST /auth/login`  
   Request body:
   ```json
   {
     "username": "yourname",
     "password": "yourpassword"
   }
   ```
   Response:
   ```json
   {
     "access_token": "<JWT_TOKEN>"
   }
   ```

3. **Token Usage:**  
   For protected routes, add this header:  
   `Authorization: Bearer <JWT_TOKEN>`

---

## API Routes & Sample Requests

| Route                | Method | Auth | Description                         |
|----------------------|--------|------|-------------------------------------|
| `/auth/register`     | POST   | ❌   | Register a new user                 |
| `/auth/login`        | POST   | ❌   | Login and receive a token           |
| `/episodes`          | GET    | ❌   | List all episodes                   |
| `/episodes/<id>`     | GET    | ❌   | Get episode with appearances        |
| `/episodes/<id>`     | DELETE | ✅   | Delete episode with its appearances |
| `/guests`            | GET    | ❌   | List all guests                     |
| `/appearances`       | POST   | ✅   | Create a new appearance             |

### Sample: Get All Episodes

**Request:**  
`GET /episodes`

**Response:**
```json
[
  {
    "id": 1,
    "title": "Episode 1",
    "date": "2024-06-01",
    "appearances": [
      {
        "guest_id": 1,
        "role": "Comedian"
      }
    ]
  }
]
```

### Sample: Create Appearance (Protected)

**Request:**  
`POST /appearances`  
Headers: `Authorization: Bearer <JWT_TOKEN>`

Body:
```json
{
  "episode_id": 1,
  "guest_id": 2,
  "role": "Musician"
}
```

**Response:**
```json
{
  "id": 5,
  "episode_id": 1,
  "guest_id": 2,
  "role": "Musician"
}
```

---

## Using Postman

1. Import the API endpoints manually or use the OpenAPI/Swagger file if available.
2. For protected routes, after registering or logging in, copy the `access_token` from the response.
3. In Postman, go to the "Authorization" tab, select "Bearer Token", and paste your token.
4. Test all endpoints as described above.

---

## GitHub Repo

[https://github.com/olella93/late-show-api-challenge](https://github.com/olella93/late-show-api-challenge)

---

**Author:**  
Richard Olella