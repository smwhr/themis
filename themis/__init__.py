from config import Config
from flask import Flask
from flask_admin import Admin
from themis.banque import BanqueView

from themis.extensions import db, login_manager, alembic

from themis.main import ThemisCoreView


def init_module(app, name, ModelView, url=None, template=None):
    return Admin(
        app,
        name=name,
        index_view=ModelView(
                template='master.html' if template is None else template,
                url=f"/{name}" if url is None else url,
                endpoint=name
        ),
        template_mode='bootstrap4'
    )


def create_app(config_class=Config):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)

    # Register extensions here
    db.init_app(app)
    login_manager.init_app(app)

    alembic.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        from themis.models.personne import Personne
        return db.session.query(Personne).get(user_id)


    app.config['FLASK_ADMIN_SWATCH'] = 'sandstone'

    main = init_module(app, 'main', ThemisCoreView, url='/')
    banque = init_module(app, 'banque', BanqueView)


    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'καλημέρα Θέμις'

    return app