from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/paco')
def paco():
    return 'My name is Paco'


# @app.route('/param')
# def param():
#     params = request.args.get('my_param', 'nothing')
#     return 'Param is = {}'.format(params)

@app.route('/param/')
@app.route('/param/<name>')
@app.route('/param/<name>/<last_name>')
@app.route('/param/<name>/<last_name>/<int:age>')  # wont accept anything else than age as int
def param(name='no name', last_name='no last name', age='no age'):
    return 'Param is = {} {} -- {}'.format(name, last_name, age)


@app.route('/render/<name>')
def render_html(name='default'):
    age = 27
    gender_list = ['male', 'female']
    gender = 'm'
    my_list = [1,2,3,4,5]
    return render_template('index.html', name_html=name, age_html=age, gender_html=gender, genderlist_html=gender_list, list_html = my_list)


app.run(debug=True)
