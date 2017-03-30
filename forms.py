from flask_wtf import FlaskForm
from wtforms import StringField, validators

class ContactForm(FlaskForm):
	name = StringField("name", [validators.InputRequired()])
	email = StringField("email", [validators.InputRequired()])