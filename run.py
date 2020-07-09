from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/paco')
def paco():
    return 'My name is Paco'


@app.route('/param')
def param():
    params = request.args.get('my_param', 'nothing')
    return 'Param is = {}'.format(params)


app.run(debug=True)
