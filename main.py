from flask import Flask, render_template, redirect


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title='Index')


@app.route('/home')
def redirect_home():
    return redirect('/')


@app.route('/english premier league')
def english_premier_league():
    return render_template('english_premier_league.html', title='English Premier League')


@app.route('/dutch eredivisie')
def dutch_eredivisie():
    return render_template('dutch_eredivisie.html', title='Dutch Eredivisie')
