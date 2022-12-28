from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from flask_alembic import Alembic
alembic = Alembic()

from flask_login import LoginManager
login_manager = LoginManager()
