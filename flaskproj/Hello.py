from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_world(name):
    if name == 'admin':
        return redirect(url_for('admin_greeting'))
    else:
        return redirect(url_for('user_greeting', name = name))

@app.route('/hello/<int:numb>')
def hello_numb(numb):
    return 'The number is ' + str(numb)

@app.route('/hello/adminMode')
def admin_greeting():
    return 'Admin Mode'

@app.route('/hello/user/<name>')
def user_greeting(name):
    return "hello " + name

if __name__ == '__main__':
    app.run(debug=True)