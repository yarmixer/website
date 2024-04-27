import sqlite3

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
db_file = 'res.db'
con = sqlite3.connect(db_file, check_same_thread=False)
cur = con.cursor()

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

    res = cur.execute(f"""SElECT count FROM class WHERE id='{param['class'][-1]}'""").fetchall()[0][0]
    cur.execute(f"""UPDATE class SET count='{res + 1}' WHERE id='{param['class'][-1]}'""").fetchall()
    con.commit()
    return f'Ваш чек:<br>' \
           f'На сумму: {summa}руб <br>' \
           f'Заказ совершен за столиком - {param["class"]}<br>' \
           f'Для оплаты перейдите по ссылке ...<br>' \
           f'Спасибо за покупку'


@app.route('/tables_counts')
def test():
    res1 = cur.execute(f"""SElECT count FROM class WHERE id='1'""").fetchall()[0][0]
    res2 = cur.execute(f"""SElECT count FROM class WHERE id='2'""").fetchall()[0][0]
    res3 = cur.execute(f"""SElECT count FROM class WHERE id='3'""").fetchall()[0][0]
    res4 = cur.execute(f"""SElECT count FROM class WHERE id='4'""").fetchall()[0][0]
    res5 = cur.execute(f"""SElECT count FROM class WHERE id='5'""").fetchall()[0][0]
    res6 = cur.execute(f"""SElECT count FROM class WHERE id='6'""").fetchall()[0][0]
    return f'Столько заказов было совершенно за этими столиками<br>' \
           f'Столик 1: {res1}<br>' \
           f'Столик 2: {res2}<br>' \
           f'Столик 3: {res3}<br>' \
           f'Столик 4: {res4}<br>' \
           f'Столик 5: {res5}<br>' \
           f'Столик 6: {res6}<br>'


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
