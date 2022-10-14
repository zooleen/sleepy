#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from dream import normalize, asleep, wakeup
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/dream', methods=['POST'])
def do_calculate() -> str:
    action = request.form['action']
    hours = int(request.form['hours'])
    minutes = int(request.form['minutes'])
    if action == "asleep":
        answer = str(asleep(hours, minutes))
        return render_template('results_asleep.html', the_title='Выспись!', the_answer=answer)
    if action == "wakeup":
        answer = str(wakeup(hours, minutes))
        return render_template('results_wakeup.html', the_title='Выспись!', the_answer=answer)

@app.route('/')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Выспись!')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
