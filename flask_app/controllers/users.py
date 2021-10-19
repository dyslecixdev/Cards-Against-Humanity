from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.episode import Episode
from flask_app.models.season import Season
from flask_app.models.show import Show
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def main_page():
    return render_template('register_and_login.html')

@app.route('/dashboard')
def dashboard_page():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': session['user_id']
    }
    return render_template('dashboard.html', user = User.read_by_id(data))

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/register', methods = ['post'])
def register():
    if not User.valid_register(request.form):
        return redirect('/')
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': bcrypt.generate_password_hash(request.form['password']),
    }
    id = User.create(data)
    session['user_id'] = id
    return redirect('/dashboard')

@app.route('/login', methods = ['post'])
def login():
    user = User.read_by_email(request.form)
    if not user:
        flash('Invalid Login!', 'login')
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Invalid Login!', 'login')
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/dashboard')