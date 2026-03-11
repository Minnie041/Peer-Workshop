import os

class Config:
    SECRET_KEY = "secretkey"
    SQLALCHEMY_DATABASE_URI = "sqlite:///workshops.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False