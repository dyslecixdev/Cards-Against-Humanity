from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.episode import Episode
from flask_app.models.season import Season
from flask_app.models.show import Show
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)