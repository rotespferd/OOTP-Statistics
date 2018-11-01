from flask import render_template

from App import App

app = App(__name__)


@app.route('/hello')
@app.route('/hello/<string:name>')
def hello(name=None):
    return render_template("hello.jinja2", name=name)


@app.route('/city/<int:city_id>')
def get_city(city_id):
    return "The city-id is %d" % city_id
