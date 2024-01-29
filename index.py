#Presenter for the landing page
from flask import request, render_template
from flask.views import MethodView


class Index(MethodView):
    def get(self):
        return render_template('index.html', isHome=True)

