from flask import Flask, url_for, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    pass


def week():
    pass


@app.route('/table', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('index.html',
                           title='Расписание 513',
                           form=form, image1='static/img/Композиция-1.gif')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')