from wtforms import form, fields, validators

from themis.extensions import db
from themis.models.personne import Personne

class RegistrationForm(form.Form):
    email = fields.StringField()
    nom = fields.StringField()
    prenom = fields.StringField()
    password = fields.PasswordField()

    def validate_login(self, field):
        if db.session.query(Personne).filter_by(email=self.email.data).count() > 0:
            raise validators.ValidationError('Email déjà connu. Essayez-vous de créer un clone ?')