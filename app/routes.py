from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForms


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Matt'}
    posts = [
        {
            'author':{'username': 'John'},
            'body':'Beautiful day in Toledo!'
        },
        {
            'author':{'username':'Susan'},
            'body':'The Avengers movie was great'
        }
    ]
    return render_template('index.html',  title = 'Home', user=user, posts= posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForms()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect("{{ url_for('index') }}")
    return render_template('login.html', title = 'Sign In', form=form)

    