from flask import Blueprint, redirect, url_for, request
from flask_admin import AdminIndexView, helpers, expose
from flask_admin.contrib import sqla
import flask_login as login
from werkzeug.security import generate_password_hash, check_password_hash

from themis.models.personne import Personne
from themis.extensions import db

from .forms.login import LoginForm
from .forms.register import RegistrationForm


class ThemisAuthenticatedView(sqla.ModelView):

    def is_accessible(self):
        return login.current_user.is_authenticated

class ThemisCoreView(AdminIndexView):

    @expose('/')
    def index(self):
        if not login.current_user.is_authenticated:
            return redirect(url_for('.login_view'))

        self._template = "moi.html"
        return super(ThemisCoreView, self).index()


    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        # handle user login
        form = LoginForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = form.get_user()
            if user is None:
                return redirect(url_for('.login_view'))
            login.login_user(user)

        if login.current_user.is_authenticated:
            return redirect(url_for('.index'))
        link = '<p>Pas encore de passeport ? <a href="' + url_for('.register_view') + '">Faîtes votre demande d\'immigration ici.</a></p>'
        self._template_args['title'] = "Se connecter"
        self._template_args['form'] = form
        self._template_args['link'] = link
        self._template = "auth.html"
        return super(ThemisCoreView, self).index()

    @expose('/register/', methods=('GET', 'POST'))
    def register_view(self):
        form = RegistrationForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = Personne()

            form.populate_obj(user)
            # we hash the users password to avoid saving it as plaintext in the db,
            # remove to use plain text:
            user.password = generate_password_hash(form.password.data)

            db.session.add(user)
            db.session.commit()

            login.login_user(user)
            return redirect(url_for('.index'))
        link = '<p>Vous avez déjà un passeport ? <a href="' + url_for('.login_view') + '">Connectez-vous ici.</a></p>'
        self._template_args['title'] = "Demande d'immigration"
        self._template_args['form'] = form
        self._template_args['link'] = link
        self._template = "auth.html"
        return super(ThemisCoreView, self).index()

    @expose('/logout/')
    def logout_view(self):
        login.logout_user()
        return redirect(url_for('.index'))




