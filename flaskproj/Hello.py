from flask import Flask, redirect, url_for, jsonify, request, render_template
import random

app = Flask(__name__)

@app.route('/hello/<name>')
def hello_world(name):
    if name == 'admin':
        return redirect(url_for('admin_greeting'))
    else:
        return redirect(url_for('user_greeting', name = name))

@app.route('/hello/<int:numb>', methods = ['GET'])
def hello_numb(numb):
    return jsonify(numb,numb+1,numb+2)

@app.route('/hello/adminMode')
def admin_greeting():
    return 'Admin Mode'

@app.route('/hello/user/<name>')
def user_greeting(name):
    return "hello " + name

@app.route('/hello/view/<name>')
def hello_view(name):
    dict = {'title':name, 'cond':1}
    return render_template('hello.html', obj = dict)

@app.route('/data')
def return_json_data():
    data = {'position1': random.randint(1,100), 'position2': random.randint(1,100), 'position3': random.randint(1,100), 'position4': random.randint(1,100)}
    return jsonify(data)

@app.route('/words')
def return_words_for_cloud():
    data = {
        'Cartão': random.randint(1,500),
        'Bom': random.randint(1,500),
        'Adorei': random.randint(1,500),
        'lento': random.randint(1,500),
        'NÃO': random.randint(1,500),
        'consegui': random.randint(1,500),
        'Excelente': random.randint(1,500),
        'xpto': random.randint(1,500),
        'banco': random.randint(1,500),
        'demorou': random.randint(1,500),
        'rápido': random.randint(1,500),
        'ruim': random.randint(1,500),
    }
    return jsonify(data)

@app.route('/charts')
def render_charts_view():
    return render_template('charts.html')

if __name__ == '__main__':
    app.run(debug=True)