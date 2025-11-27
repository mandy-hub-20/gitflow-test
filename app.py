from flask import Flask, render_template

app = Flask(__name__)

from datetime import datetime



@app.route('/')
def home():
    return render_template('index.html', message="Heyyy, Home Flask!")

@app.route('/showdate')
def showdate():
    curr_datetime = datetime.now()
    return render_template('index.html', message="the time now is :", curr_date=curr_datetime)


if __name__ == '__main__':
    app.run(debug=True)