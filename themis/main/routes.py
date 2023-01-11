from themis.main import bp

from flask import redirect, url_for, request, render_template, flash

import flask_login as login
from werkzeug.security import generate_password_hash, check_password_hash

from .models.personne import Personne
from themis.extensions import db

from .forms.login import LoginForm
from .forms.register import RegistrationForm


@bp.route('/')
def index():
    if not login.current_user.is_authenticated:
        return redirect(url_for('.login_view'))
    return render_template("main/moi.html",crumbs=["Général", "Moi"])


@bp.route('/login/', methods=('GET', 'POST'))
def login_view():
    # handle user login
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = form.get_user()
        if user is not None and check_password_hash(user.password, form.password.data):
            login.login_user(user)
        else:
            flash(f"Email inconnu ou mot de passe incorrect.", "danger")
            return redirect(url_for('.login_view'))

    if login.current_user.is_authenticated:
        return redirect(url_for('.index'))
    
    link = '<p>Pas encore de passeport ? <a href="' + url_for('.register_view') + '">Faîtes votre demande d\'immigration ici.</a></p>'
    
    return render_template("auth/login.html", 
                            title="Se connecter", 
                            form = form,
                            link=link
                        )

@bp.route('/register/', methods=('GET', 'POST'))
def register_view():
    form = RegistrationForm(request.form)
    if form.validate_on_submit():
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
    
    return render_template("auth/login.html", 
                            title="Demande d'immigration", 
                            infotext="Veuillez remplir le formulaire d'immigration.",
                            form = form,
                            link=link
                        )

@bp.route('/logout/')
def logout():
    login.logout_user()
    return redirect(url_for('.index'))




