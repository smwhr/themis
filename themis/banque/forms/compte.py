from flask_wtf import FlaskForm
from wtforms import fields, validators

from themis.extensions import db

class CreationForm(FlaskForm):
    nom = fields.StringField(label="Libellé du compte")


class DeletionForm(FlaskForm):
    compte_id = fields.SelectField(label="Compte à supprimer")

    def populate(self, deletable):
            self.compte_id.choices = deletable


class TransactionForm(FlaskForm):
    depuis_id = fields.SelectField(label="Depuis le compte")
    vers_id   = fields.SelectField(label="Vers le compte")
    montant   = fields.IntegerField(label="Montant")

    def populate(self, depuis, vers):
        self.depuis_id.choices = depuis
        self.vers_id.choices = vers