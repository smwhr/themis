from flask import Blueprint

bp = Blueprint('banque', __name__)

from . import routes