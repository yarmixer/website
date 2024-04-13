from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('main.html', title='Ресторан')


@app.route('/menu')
def menu():
    return render_template('menu.html', title='Меню ресторана')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')