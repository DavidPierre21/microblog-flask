from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'David'}

    posts = [
        {
            'author': {'username': 'Michelangelo'},
            'body': 'Beautiful day in Recife!'
        },
        {
            'author': {'username': 'Rafael'},
            'body': 'Rainy day in Recife!'
        },
        {
            'author': {'username': 'Leonardo'},
            'body': 'Hot day in Recife!'
        },
        {
            'author': {'username': 'Donatello'},
            'body': 'Its day in Recife!'
        }
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)
