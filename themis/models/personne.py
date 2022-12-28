from themis.extensions import db
from flask_login.mixins import UserMixin
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from .communaute import Communaute
from themis.banque.models.compte import Compte

class Personne(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255))
    nom = db.Column(db.String(255))
    password = db.Column(db.Text)
    prenom = db.Column(db.String(255))

    communaute_id = db.Column(db.Integer, ForeignKey("communaute.id"))
    communaute = relationship("Communaute", back_populates="membres")


    ### Relationship
    comptes = relationship("Compte", back_populates="personne")


    @property
    def full_name(self):
        return f"{self.prenom} {self.nom}".strip()

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return f'<Personne "{self.full_name}">'