import importlib
from config import Config
from flask import Flask

from themis.extensions import db, login_manager, migrate



def init_module(app, name, url=None):
    module = importlib.import_module(f'themis.{name}')
    app.register_blueprint(module.bp, 
                           url_prefix=url if url is not None else f"/{name}"
                        )


def create_app(config_class=Config):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)

    # Register extensions here
    db.init_app(app)
    login_manager.init_app(app)

    

    @login_manager.user_loader
    def load_user(user_id):
        from themis.main.models.personne import Personne
        return db.session.query(Personne).get(user_id)


    app.config['FLASK_ADMIN_SWATCH'] = 'sandstone'

    main = init_module(app, 'main', url='/')
    banque = init_module(app, 'banque')

    migrate(app)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'καλημέρα Θέμις'

    return app