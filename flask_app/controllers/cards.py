from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.card import Card
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# ADD INFO
@app.route('/winner/cards')
def winner_cards():
    if 'user_id' not in session:
        return redirect('/logout') 
    return render_template("winner_cards.html")

# ADD INFO
@app.route('/winner')
def winner():
    if 'user_id' not in session:
        return redirect('/logout') 
    return render_template ("winner.html") 

# Adds a new card to the cards table in the database, and redirects them to the card winners page.
@app.route('/create_card', methods = ['post'])
def create_card():
    if 'user_id' not in session:
        return redirect('/logout') 
    if not Card.validate_card(request.form): # ADD INFO
        return redirect('/winner')
    data = {
        'card_name': request.form['card_name'],
        'card_statement': request.form['card_statement']
    }
    id = Card.create_card(data)
    session['user_id'] = id
    return redirect('/winner/cards')  