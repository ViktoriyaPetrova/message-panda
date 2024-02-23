#Register routes and assign presenter go routes 
import flask
import os
from flask_wtf.csrf import CSRFProtect 
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from index import Index
from messageGenerator import MessageGenerator

flask_secret_key = os.getenv('FLASK_SECRET_KEY')

app = flask.Flask(__name__) 
app.config['SECRET_KEY'] = flask_secret_key
csrf = CSRFProtect(app)

# Initialize Limiter
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["300 per day", "100 per hour"]
)

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
@app.errorhandler(429)
def rate_limit_exceeded(e):
    return flask.render_template('429.html'), 429

#Run program on localhost port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
