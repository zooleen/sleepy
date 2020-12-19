from dream import normalize, asleep, wakeup
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'

@app.route('/dream', methods=['POST'])
def do_calculate() -> str:
    action = request.form['action']
    hours = int(request.form['hours'])
    minutes = int(request.form['minutes'])
    if action == "asleep":
        return str(asleep(hours, minutes))
    if action == "wakeup":
        return str(wakeup(hours, minutes))

@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Выспись!')

app.run(debug=True)
