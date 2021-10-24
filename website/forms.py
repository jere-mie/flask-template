from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, FileField, DecimalField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError, NumberRange
from website.models import User

class Register(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=20)])    
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=20)])
    confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    # validates the username entered
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is already taken')

class Login(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    rememberMe = BooleanField('Remember Me')
    submit = SubmitField('Sign In')  