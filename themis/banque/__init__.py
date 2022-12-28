from flask_admin import expose
from flask_admin import AdminIndexView
import flask_login as login



class BanqueView(AdminIndexView):

    def is_accessible(self):
        return login.current_user.is_authenticated

    @expose('/')
    def index(self):
        self._template = "banque/index.html"
        return super(BanqueView, self).index()