from dream import normalize, asleep, wakeup
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'

@app.route('/dream', methods=['POST'])
def do_calculate() -> str:
    return str(asleep(7,40))

@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Выспись!')

app.run(debug=True)
