from themis.extensions import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from .transaction import Transaction

class Compte(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(255))
    personne_id = db.Column(db.Integer, ForeignKey("personne.id"))
    personne = relationship("Personne", back_populates="comptes")

    transactions = relationship("Transaction", back_populates="compte")

