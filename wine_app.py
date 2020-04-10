from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c527a44ec33905f764d09b271dbb0fa4052588e0da143a1ac2765944693358e3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# to generate a temporary secret key open cmd prompt run idle and
db = SQLAlchemy(app)
#import secrets
# secrets.token_hex(# value)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(60), nullable=False)
    lastname = db.Column(db.String(60), nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    username = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.firstname}', '{self.lastname}', '{self.username}', '{self.email}', '{self.image_file}') "


class Post(db.Model):


test_data = [
    {
        'name': 'wine1',
        'color': 'red',
        'type': 'big grape',
        'origin': 'Germany',
        'taste': 'sweet'
    },
    {
        'name': 'wine2',
        'color': 'white',
        'type': 'yellow grape',
        'origin': 'Austria',
        'taste': 'bitter'
    },
    {
        'name': 'wine3',
        'color': 'red',
        'type': 'dark grape',
        'origin': 'Australia',
        'taste': 'motor oil'
    }

]


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/colors")
def colors():
    return render_template('colors.html', title='Wine Data', test_data=test_data)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@wt.com' and form.password.data == 'password':
            flash('You have been Logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash(
                'Login Credintials are incorrect, Please check username and password', 'danger')
    return render_template('login.html', title='Register', form=form)


if __name__ == '__main__':
    app.run(debug=True)
