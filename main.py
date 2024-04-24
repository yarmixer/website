from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('main.html', title='Ресторан')


@app.route('/menu', methods=['POST', 'GET'])
def menu():

    if request.method == 'GET':
        return render_template('menu.html', title='Меню ресторана')

    elif request.method == 'POST':
        print(request.form['breakfast1'])
        print(request.form['class'])
        return "Форма отправлена"


@app.route('/check')
def check():
    return 'Ваш чек'


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')