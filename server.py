from flask_app.controllers import users
from flask_app.controllers import shows
from flask_app.controllers import seasons
from flask_app.controllers import episodes
from flask_app import app

if __name__ == '__main__':
    app.run(debug=True)