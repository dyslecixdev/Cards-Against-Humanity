from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

# Declares the database name.
DATABASE = "user_schema_cah"

# Card table with all of its attributes.
class Card:
    def __init__(self, data):
        self.id = data['id']
        self.card_name = data['card_name']
        self.card_statement = data['card_statement']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    # I have access to user_id, how can I use user_id to grab that user's each tree, how can I use tree's user_id to grab that user
    @property
    def creator(self):
        return User.read_by_id({'id': self.user_id}) 

    # Creates a card, and inserts their data in the cards table.
    @classmethod
    def create_card(cls, data):
        query = 'INSERT INTO cards (card_name, card_statement) VALUES (%(card_name)s, %(card_statement)s);'
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    # Selects all of the cards in the cards table.
    @classmethod
    def read_all_cards(cls):
        query = 'SELECT * FROM cards;'
        results = connectToMySQL(DATABASE).query_db(query)
        cards = []
        for row in results:
            cards.append(cls(row))
        return cards

    # Selects one card from the cardss table by their card_name.
    @classmethod
    def read_by_card_name(cls, data):
        query = 'SELECT * FROM cards WHERE card_name = %(card_name)s;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])

    # Selects one card from the cards table by their id.
    @classmethod
    def read_card_by_id(cls, data):
        query = 'SELECT * FROM cards WHERE id = %(id)s;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])

    # Generates a flash message on the card winner page if certain requirements aren't met.
    @staticmethod
    def validate_card(card):
        is_valid = True
        if len(card['card_name']) < 3: 
            is_valid = False
            flash("Card name must be at least 3 characters", "card")
        if len(card['card_statement']) < 8:
            is_valid = False
            flash("Card statement must be at least 3 characters", "card")
        return is_valid   