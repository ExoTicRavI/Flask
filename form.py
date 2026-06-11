from flask_wtf import FlaskForm
from wtforms import (
    StringField, 
    SubmitField,
    PasswordField,
    RadioField,
    SelectField,
    BooleanField)
from wtforms.validators import DataRequired



class NameForm(FlaskForm):
    name = StringField('Enter your name', validators=[DataRequired()])
    submit = SubmitField('Submit')