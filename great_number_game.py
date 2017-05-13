from random import randrange
from flask import Flask, request, redirect, render_template, session
app = Flask(__name__)
app.secret_key = "parseltongue"

@app.route('/')
def number_game():
    if session.get('number', None) == None:
        session['number'] = randrange(1, 101)   # create & store random num
        session['low'] = 'hideme'               # hide 'too low' error message
        session['high'] = 'hideme'              # hide 'too high' error message
        session['player_guess'] = 'showme'        # set input bar to visible
        session['play_again'] = 'hideme'          # hide 'play again' message
    return render_template('great_number_game.html')

@app.route('/guess', methods=['POST'])
def take_guess():
    guess = int(request.form.get('guess', None))
    sesh = int(session.get('number', None))
    if guess == sesh:                           # if user guess == random num
        if session['high'] == 'showme':
            session['high'] = 'hideme'          # hide 'too high' error message
        if session['low'] == 'showme':  
            session['low'] = 'hideme'           # hide 'too low' error message
        session['player_guess'] = 'hideme'      # hide user input bar
        session['play_again'] = 'showme'        # show 'play again' message

    elif guess > sesh:                          # if user guess > random num
        if session['low'] == 'showme':
            session['low'] = 'hideme'           # hide 'too low' error message
        session['high'] = 'showme'              # show 'too high' error message

    elif guess < sesh:                          # if user guess < random num
        if session['high'] == 'showme':
            session['high'] = 'hideme'          # hide 'too high' error message
        session['low'] = 'showme'               # show 'too low' error message

    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset_game():
    session.pop('number')                       # remove number from session
    return redirect('/')

app.run(debug = True)