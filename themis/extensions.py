from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from flask_migrate import Migrate, upgrade
def migrate(app):
    m = Migrate(app, db)
    with app.app_context():
        upgrade()
    return m

from flask_login import LoginManager
login_manager = LoginManager()
