"""
http://flask.pocoo.org/docs/1.0/quickstart/
export/set FLASK_APP=
export/set FLASK_ENV=development
flask run
"""
from flask import Flask, request
import temperature
app = Flask(__name__)


@app.route('/')
def hello_world():
    return """
<form method="POST">
Please give me a
 temperature in fahrenheit: 
    <input name="temp">
    <input type="submit">
</form>
"""


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['temp']
    fahr = float(text)
    celsius = temperature.fahr_to_celsius(fahr)
    return f"Your temperature was: {text}; Celsius is: {celsius}"





