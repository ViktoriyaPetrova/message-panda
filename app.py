#Register routes and assign presenter go routes 
import flask
import os
from flask_wtf.csrf import CSRFProtect 
from index import Index
from messageGenerator import MessageGenerator

flask_secret_key = os.getenv('FLASK_SECRET_KEY')

app = flask.Flask(__name__) 
app.config['SECRET_KEY'] = flask_secret_key
csrf = CSRFProtect(app)

#Landing page route
app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=['GET'])
#Main app functionality route
app.add_url_rule('/message-generator',
                 view_func=MessageGenerator.as_view('message-generator'),
                 methods=['GET','POST'])
@app.errorhandler(404)
def page_not_found(e):
    return flask.render_template('404.html'), 404

#Run program on localhost port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
