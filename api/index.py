from themis import create_app
from flask_migrate import upgrade

app = create_app()
upgrade()