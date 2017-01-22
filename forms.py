from flask_wtf import Form 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
    first_name = StringField('First name', validators=[DataRequired("You did not enter your first name")])
    last_name = StringField('Last name', validators=[DataRequired("You did not enter your last name")])
    email = StringField('Email', validators=[DataRequired("You did not enter you email"), Email("Please enter a valid email address.")])
    password = PasswordField('Password', validators=[DataRequired("You cannot signup without a password!"), Length(min=6, message="Password must be at least 6 characters")])
    submit = SubmitField('Sign up')