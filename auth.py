from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from .models import User, UserCategory
from . import db
import string
import random

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    # login code goes here
    form_email = request.form.get('input_email').lower()
    form_password = request.form.get('input_password')

    user = User.query.filter_by(user_email=form_email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(pwhash=user.user_password, password=form_password):
        flash('Email or Password is incorrect')
        # if the user doesn't exist or password is wrong, reload the page
        return redirect(url_for('auth.login'))

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=False)
    return redirect(url_for('main.home'))


@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    # code to validate and add user to database goes here
    form_firstName = request.form.get('input_firstname')
    form_lastName = request.form.get('input_lastname')
    form_password = request.form.get('input_password')
    form_email = request.form.get('input_email').lower()
    
    #To make sure that randomly generated id is not already present

    while(True):
        assigned_id = str(''.join(random.choices(string.digits, k = 8)))
        
        if User.query.filter_by(user_id=assigned_id).first():
            continue
        else:
            break
        
    # if this returns a user, then the email already exists in database
    user = User.query.filter_by(user_email=form_email).first()

    if user:  # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(user_id=assigned_id, user_email=form_email, user_firstname=form_firstName,
                    user_lastname=form_lastName, user_password=generate_password_hash(form_password, method='sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    # Add the user in user category DB
    db.session.add(UserCategory(user_id=assigned_id))
    db.session.commit()

    return redirect(url_for('auth.login'))



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

# Adding a route for 404 page, any unreachable page, will end up redirecting here


@auth.errorhandler(404)
def invalid_route():
    return render_template('404.html')
