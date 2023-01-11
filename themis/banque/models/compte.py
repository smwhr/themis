from themis.extensions import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from .transaction import Transaction

class Compte(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(255))
    personne_id = db.Column(db.Integer, ForeignKey("personne.id"))
    personne = relationship("Personne", back_populates="comptes")

    montant = db.Column(db.Integer, nullable=False, default=0, server_default='0')

    transactions = relationship("Transaction", back_populates="compte")
    last_transaction = db.Column(db.DateTime)

