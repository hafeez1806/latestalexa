import logging
from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.launch
def new_game():
 welcome_msg = render_template('welcome') #welcome_msg
 return question(welcome_msg)

@ask.intent("YesIntent")
def next_round():
 numbers = [randint(0, 9) for _ in range(3)] #Random 3 numbers in between 0 to 9
 round_msg = render_template('round', numbers=numbers)
 session.attributes['numbers'] = numbers[::-1]  #reversing the numbers
 return question(round_msg)

@ask.intent("AnswerIntent", convert={'first': int})
def answer(first):
 print(first)
 winning_numbers = ''.join(list(map(str,session.attributes['numbers']))) #testing the winning numbers with given numbers
 print("this is winning number:",winning_numbers)
 if str(first) == winning_numbers:
  msg = render_template('win')
 else:
  msg = render_template('lose')
 return statement(msg)

if __name__ == '__main__':
 app.run(debug=True)
