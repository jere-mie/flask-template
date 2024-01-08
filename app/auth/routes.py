from flask import render_template
from app.auth import bp

@bp.route('/login')
def login():
    return render_template('temp.html')

@bp.route('/logout')
def logout():
    return render_template('temp.html')

@bp.route('/register')
def register():
    return render_template('temp.html')
