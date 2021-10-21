from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

# Declares the database name.
DATABASE = "user_schema_cah"

# Users table with all of its attributes.
class User:
    def __init__(self, data):
        self.id = data['id']
        self.character_name = data['character_name']
        self.hash_pw = data['hash_pw']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Creates a user, and inserts their data in the users table.
    @classmethod
    def create(cls, data):
        query = 'INSERT INTO users (character_name, hash_pw) VALUES (%(character_name)s, %(hash_pw)s);'
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    # Selects all of the users in the users table.
    @classmethod
    def read_all(cls):
        query = 'SELECT * FROM users;'
        results = connectToMySQL(DATABASE).query_db(query)
        users = []
        for row in results:
            users.append(cls(row))
        return users

    # Selects one user from the users table by their character_name.
    @classmethod
    def read_by_character_name(cls, data):
        query = 'SELECT * FROM users WHERE character_name = %(character_name)s;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])

    # Selects one user from the users table by their id.
    @classmethod
    def read_by_id(cls, data):
        query = 'SELECT * FROM users WHERE id = %(id)s;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])

    # Generates a flash message on the registration/login page if certain requirements aren't met.
    @staticmethod
    def valid_register(user):
        is_valid = True
        query = 'SELECT * FROM users WHERE character_name = %(character_name)s;'
        result = connectToMySQL(DATABASE).query_db(query, user)
        if len(user['character_name']) < 2:
            flash('First name must be at least 3 characters.', 'register')
            is_valid = False
        if len(result) >= 1:
            flash('Username is already taken.', 'register')
            is_valid = False
        if len(user['hash_pw']) < 3:
            flash('Password must be at least 3 characters.', 'register')
            is_valid = False
        if user['hash_pw'] != user['confirm']:
            flash('Passwords do not match.', 'register')
        return is_valid 