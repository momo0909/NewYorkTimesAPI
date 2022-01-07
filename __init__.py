from flask import Flask


app = Flask(__name__)

app.config['SECRET_KEY'] = "project"

from Project2_Flask import routes