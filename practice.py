import flask
import flask.views
import os

app = flask.Flask(__name__)
app.secret_key = "chachonga"

class View(flask.views.MethodView):
    def get(self):
        return flask.render_template('index.html')
#        return "Hello, world!"

    def post(self):
        result = eval(flask.request.form['mkrequest'])
        flask.flash(result)
        return self.get()

app.debug = True
app.add_url_rule('/', view_func=View.as_view('main'),
        methods = ['GET', 'POST'])
app.run()
