from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('main.html', title='Ресторан')


@app.route('/menu', methods=['GET', 'POST'])
def menu():
    if request.method == 'GET':
        return render_template('menu.html', title='Меню ресторана')
    elif request.method == 'POST':
        param = {'breakfast1': request.form['breakfast1'], 'breakfast2': request.form['breakfast2'],
                 'breakfast3': request.form['breakfast3'], 'dinner1': request.form['dinner1'],
                 'dinner2': request.form['dinner2'], 'dinner3': request.form['dinner3'],
                 'pdinner1': request.form['pdinner1'], 'pdinner2': request.form['pdinner2'],
                 'pdinner3': request.form['pdinner3'], 'class': request.form['class']}
        print(param)
        return redirect(url_for('check', param=param))


@app.route('/check/<param>')
def check(param):
    param = eval(param)
    summa = int(param['breakfast1']) * 450 + int(param['breakfast2']) * 590 + int(param['breakfast3']) * 300 +\
    int(param['dinner1']) * 900 + int(param['dinner2']) * 2200 + int(param['dinner3']) * 450 + int(param['pdinner1']) * 300 \
            + int(param['pdinner2']) * 590 + int(param['pdinner3']) * 250
    print(summa)
    return f'Ваш чек:<br>' \
           f'На сумму: {summa}руб <br>' \
           f'Заказ совершен за столиком - {param["class"]}<br>' \
           f'Для оплаты перейдите по ссылке ...<br>' \
           f'Спасибо за покупку'


@app.route('/test')
def test():
    return render_template('test.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
