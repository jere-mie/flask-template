from flask import render_template, url_for, flash, redirect, request
from website import app, db
from website.forms import Register, Login
from website.models import User
from flask_login import login_user, current_user, logout_user, login_required
import os
import bcrypt

@app.route('/home', methods=['GET'])
@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    # we redirect the user if they're already authenticated
    if current_user.is_authenticated:
        flash('You are already authenticated','success')
        return redirect(url_for('home'))

    form = Register() # registration form

    # if the form is submitted and validated, we add the user
    if form.validate_on_submit():
        hashed = bcrypt.hashpw(form.password.data.encode('utf-8'), bcrypt.gensalt())
        user = User(username=form.username.data, password=hashed)
        db.session.add(user)
        db.session.commit()
        flash(f'Created account for {form.username.data}. You may now log in.', 'success')
        return redirect(url_for('login'))

    # else we return the register page
    return render_template("register.html", form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # we redirect the user if they're already authenticated
    if current_user.is_authenticated:
        flash('You are already authenticated','success')
        return redirect(url_for('home'))

    form = Login()
    # if the form is submitted and validated, we login the user
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.checkpw(form.password.data.encode('utf-8'), user.password):
            login_user(user, remember=form.rememberMe.data)
            return redirect(url_for('home'))
        else:
            flash('Error Logging In', 'danger')
    return render_template("login.html", form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))