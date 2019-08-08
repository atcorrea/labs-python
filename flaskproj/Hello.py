from flask import Flask, redirect, url_for, jsonify, request, render_template
import random

app = Flask(__name__)

@app.route('/hello/<name>')
def hello_world(nome):
    if nome == 'admin':
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
        'fila': random.randint(1,500),
        'atendimento': random.randint(1,500),
        'amei': random.randint(1,500),
        'maravilhoso': random.randint(1,500),
        'moroso': random.randint(1,500),
        'crítico': random.randint(1,500),
        'importante': random.randint(1,500),
        'mais': random.randint(1,500),
        'totalmente': random.randint(1,500),
        'claro': random.randint(1,500),
        'melhor': random.randint(1,500),
        'pior': random.randint(1,500),
        'bravo': random.randint(1,500),
        'animada': random.randint(1,500),
        'Correria': random.randint(1,500),
        'outro': random.randint(1,500),
        'pode': random.randint(1,500),
        'melhorar': random.randint(1,500),
        'texto': random.randint(1,500),
        'andando': random.randint(1,500),
        'pulo': random.randint(1,500),
        'atendente': random.randint(1,500),
        'fraco': random.randint(1,500),
        'forte': random.randint(1,500),
        'passagem': random.randint(1,500),
        'next': random.randint(1,500),
        'regular': random.randint(1,500),
        'feliz': random.randint(1,500),
    }
    return jsonify(data)

@app.route('/charts')
def render_charts_view():
    return render_template('charts.html')

@app.route('/dashboard')
def render_dashboard_view():
    return render_template('dashboard.html')

@app.route('/dashboard2')
def render_dashboard2_view():
    return render_template('dashboard2.html')

if __name__ == '__main__':
    app.run(debug=True)