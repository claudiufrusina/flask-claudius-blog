from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import BooleanField, PasswordField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired("Campo obbligatorio!")])
    password = PasswordField('Password', validators=[DataRequired("Campo obbligatorio!")])
    remember_me = BooleanField('Ricordami')
    submit = SubmitField('Login')

class PostForm(FlaskForm):
    title = StringField('Titolo', 
        validators=[DataRequired("Campo obbligatorio!"), Length(min=3, max=120, 
        message="Assicurati che il titolo abbia tra 3 e 120 char")])
    description = TextAreaField('Descrizione')
    body = TextAreaField('Contenuto', 
        validators=[DataRequired("Campo obbligatorio!"), Length(min=3, max=240,
        message="Assicurati che il contenuto non superi i 240 char")])
    image = FileField('Copertina articolo', validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    submit = SubmitField('Pubblica Post')

