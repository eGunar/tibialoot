from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

class ContactForm(FlaskForm):
	name = StringField("name", [validators.InputRequired()])
	email = StringField("email", [validators.InputRequired()])


class LoginForm(FlaskForm):
	password = PasswordField("password", [validators.InputRequired()])