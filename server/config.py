import os

class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://citikom@localhost:5432/late_show_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "super-secret-key"
    JWT_SECRET_KEY = "jwt-secret-key"
