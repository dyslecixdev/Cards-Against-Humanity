from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.card import Card
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# Renders the card winners page.
@app.route('/winner/cards')
def winner_cards():
    if 'user_id' not in session:
        return redirect('/logout') 
    data = {
        'id': session['user_id']
    }
    return render_template("winner_cards.html", cards = Card.read_all_cards(), user = User.read_by_id(data))

# Renders the winner page.
@app.route('/winner')
def winner():
    if 'user_id' not in session:
        return redirect('/logout') 
    data = {
        'id': session['user_id']
    }

    return render_template ("winner.html", user = User.read_by_id(data))

# Renders the loser page.
@app.route('/loser')
def loser():
    if 'user_id' not in session:
        return redirect('/logout') 
    data = {
        'id': session['user_id']
    }
    return render_template ("loser.html", user = User.read_by_id(data))

# Adds a new card to the cards table in the database, and redirects them to the card winners page.
@app.route('/create_card', methods = ['post'])
def create_card():
    if 'user_id' not in session:
        return redirect('/logout') 
    if not Card.validate_card(request.form):
        return redirect('/winner')
    data = {
        'card_name': request.form['card_name'],
        'card_statement': request.form['card_statement'],
        "user_id": session['user_id']
    }
    Card.create_card(data)
    return redirect('/winner/cards')  