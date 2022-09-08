# Run in terminal: flask  --debug run
from flask import render_template, Flask, url_for

app = Flask(__name__)

teste = 10


@app.route('/')
@app.route('/<name>')
def hello(name=''):
    return render_template('index.html', res={'name': name, 'teste': teste})
