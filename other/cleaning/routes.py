from flask import render_template, url_for, flash, redirect
from wine_app import app
from wine_app.forms import RegistrationForm, LoginForm
from wine_app.models import User, Post
#import secrets
# secrets.token_hex(# value)
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
