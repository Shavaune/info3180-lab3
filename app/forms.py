
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Email

class ContactForm(FlaskForm):

    user_name = StringField('Name', validators=[InputRequired()])
    user_email = StringField('E-mail', validators=[InputRequired(), Email()])
    mail_subject = StringField('Subject', validators=[InputRequired()])
 
    message = TextAreaField('Message', validators=[InputRequired()])

    submit = SubmitField('Submit')