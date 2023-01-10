from wtforms import fields, validators

from flask_wtf import FlaskForm
from werkzeug.security import check_password_hash

from themis.extensions import db
from ..models.personne import Personne

class LoginForm(FlaskForm):
    email = fields.StringField()
    password = fields.PasswordField()

    def validate_login(self, field):
        user = self.get_user()

        if user is None:
            raise validators.ValidationError('Invalid user')

        # we're comparing the plaintext pw with the the hash from the db
        if not check_password_hash(user.password, self.password.data):
        # to compare plain text passwords use
        # if user.password != self.password.data:
            raise validators.ValidationError('Invalid password')

    def get_user(self):
        return db.session.query(Personne).filter_by(email=self.email.data).first()