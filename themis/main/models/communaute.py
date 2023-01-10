from themis.extensions import db
from sqlalchemy.orm import relationship

class Communaute(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(255))
    membres = relationship("Personne",  back_populates="communaute")
    
    def __repr__(self):
        return f'<Communauté "{self.nom}">'