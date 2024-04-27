from flask import Flask, render_template, request, redirect, url_for
from bs4 import BeautifulSoup


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('main.html', title='Ресторан')


@app.route('/menu', methods=['GET', 'POST'])
def menu():
    if request.method == 'GET':
        return render_template('menu.html', title='Меню ресторана')
    elif request.method == 'POST':
        data = request.json
        print(data)
        html = open('templates/menu.html')
        soup = BeautifulSoup(html, 'html.parser')
        a1, a2, a3, a4, a5, a6, a7, a8, a9 = soup.find('span', 'count1').text,\
            soup.find('span', 'count2').text, soup.find('span', 'count3').text,\
            soup.find('span', 'count4').text, soup.find('span', 'count5').text,\
            soup.find('span', 'count6').text, soup.find('span', 'count7').text,\
            soup.find('span', 'count8').text, soup.find('span', 'count9').text
        print(a1, a2, a3, a4, a5, a6, a7, a8, a9)
        return redirect(url_for('check', a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, a6=a6, a7=a7, a8=a8, a9=a9))


@app.route('/check')
def check(a1, a2, a3, a4, a5, a6, a7, a8, a9):
    print(a1, a2, a3, a4, a5, a6, a7, a8, a9)
    return 'ok'


@app.route('/test')
def test():
    return render_template('test.html')





if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')