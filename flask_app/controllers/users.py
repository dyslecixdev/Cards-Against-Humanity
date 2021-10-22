from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.card import Card
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# Renders the registration/login page when you open this in the default browser.
@app.route('/')
def main_page():
    return render_template('register_and_login.html')

# Renders the dashboard page.
@app.route('/dashboard')
def dashboard_page():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': session['user_id']
    }
    return render_template('dashboard.html', user = User.read_by_id(data))

# Logs out the user, and redirects them to the registration/login page.
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

# Adds a user's data to the users table in the database, and redirects them to the dashboard page.
@app.route('/register', methods = ['post'])
def register():
    if not User.valid_register(request.form):
        return redirect('/')
    data = {
        'character_name': request.form['character_name'],
        'hash_pw': bcrypt.generate_password_hash(request.form['hash_pw']),
    }
    id = User.create(data)
    session['user_id'] = id
    return redirect('/dashboard')

# Compares a user's login data with their registered data from the users table, and redirects them to the dashboard page.
@app.route('/login', methods = ['post'])
def login():
    user = User.read_by_character_name(request.form)
    if not user:
        flash('Invalid Login!', 'login')
        return redirect('/')
    if not bcrypt.check_password_hash(user.hash_pw, request.form['hash_pw']):
        flash('Invalid Login!', 'login')
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/dashboard') 