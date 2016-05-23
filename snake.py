from flask import Flask
app = Flask(__name__)

@application.route("/")
def gravity_snake():
    return render_template('gravity_snake.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
