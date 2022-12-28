from themis.extensions import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Transaction(db.Model):
    compte_id = db.Column(db.Integer, ForeignKey("compte.id"))
    compte = relationship("Compte", back_populates="transactions")

    date = db.Column(db.DateTime)
    montant = db.Column(db.Integer)
    libelle = db.Column(db.Text)