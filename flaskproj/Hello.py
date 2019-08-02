from flask import Flask, redirect, url_for, jsonify, request, render_template

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

if __name__ == '__main__':
    app.run(debug=True)