from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)

class Episode:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.number = data['number']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']