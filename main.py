from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html', title="Index")


@app.route("/home")
def redirect_home():
    return redirect('/')


@app.route("/about")
def about():
    return render_template('about.html',  title='About')


@app.route("/soccerclubs")
def soccerclubs():
    return render_template("soccerclubs.html", title="SoccerClubs")


with app.test_request_context():
    print(url_for('index'))
    print(url_for('soccerclubs'))
    print(url_for('about'))


if __name__ == '__main__':
    app.run()
