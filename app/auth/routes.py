import bcrypt
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required

from app import db
from app.auth import bp
from app.auth.helpers import validate_register_form
from app.models import User

@bp.route('/register', methods=['GET', 'POST'])
def register():
    # we redirect the user if they're already authenticated
    if current_user.is_authenticated:
        flash('You are already authenticated','success')
        return redirect(url_for('main.index'))

    # if the form is submitted and validated, we add the user
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        messages = validate_register_form(username, password)
        for m in messages:
            flash(m, 'danger')
        if messages:
            return redirect(url_for('auth.register'))

        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user = User(username=username, password=hashed)
        db.session.add(user)
        db.session.commit()
        flash(f'Created account for {username}. You may now log in.', 'success')
        return redirect(url_for('auth.login'))

    # else we return the register page
    return render_template("register.html")

@bp.route('/login', methods=['GET', 'POST'])
def login():
    # we redirect the user if they're already authenticated
    if current_user.is_authenticated:
        flash('You are already authenticated','danger')
        return redirect(url_for('main.index'))

    # if the form is submitted and validated, we login the user
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        remember_me = request.form.get('rememberme')
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.checkpw(password.encode('utf-8'), user.password):
            login_user(user, remember=remember_me)
            flash('Successfully logged in!', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Error Logging In', 'danger')
    return render_template("login.html")

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Successfully logged out!', 'success')
    return redirect(url_for('main.index'))
