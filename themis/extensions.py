from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from flask_migrate import Migrate
migrate = lambda app: Migrate(app, db)

from flask_login import LoginManager
login_manager = LoginManager()
