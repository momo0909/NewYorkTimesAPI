from wtforms import SelectField, StringField, SubmitField,IntegerField
from flask_wtf import FlaskForm


class articleForms(FlaskForm):
    section = SelectField("section",
                          choices=[("arts", "Top newly articles about the arts"),
                                   ("sports", "Top newly articles about sports"),
                                   ("health", "Top newly articles about health")])
    genre = SelectField("genre",choices=[("Hardcover Fiction","Hardcover Fiction"),
                                         ("Hardcover NonFiction","Hardcover NonFiction"),
                                         ("Manga","Manga"),
                                         ("Picture Books","Picture Books")])

    submit = SubmitField("Submit")