from themis.banque import bp

from flask import redirect, url_for, request, render_template, flash
import flask_login as login


from themis.extensions import db


from .models.compte import Compte
from .forms.compte import CreationForm, DeletionForm, TransactionForm

@bp.route('/')
@login.login_required
def index():
    comptes = db.session.query(Compte).filter_by(personne=login.current_user).all()

    form = CreationForm()
    delete_form = DeletionForm()

    return render_template("banque/index.html", 
                           comptes=comptes,
                           form=form,
                           delete_form=delete_form,
                           crumbs=["Banque", "Comptes"])


@bp.route('/transaction', methods=('GET', 'POST'))
@login.login_required
def transaction():
    depuis = db.session.query(Compte).filter_by(personne=login.current_user).all()
    vers =  db.session.query(Compte).all()

    form = TransactionForm(request.form)
    form.populate([(d.id, d.nom) for d in depuis], 
                   [(v.id, v.nom) for v in vers])


    if form.validate_on_submit():
        compte_depuis = db.session.query(Compte).filter_by(id=form.depuis_id.data).first()
        compte_vers = db.session.query(Compte).filter_by(id=form.vers_id.data).first()
        montant = form.montant.data
        flash(f"Transaction enregistrée : de {compte_depuis.nom} ({compte_depuis.personne.full_name})"
              + f" vers {compte_vers.nom} ({compte_depuis.personne.full_name}) : {montant} Y$", "success")
        return redirect(url_for('banque.index'))

    return render_template("banque/transaction.html", 
                           comptes=depuis,
                           form=form,
                           crumbs=["Banque", "Transaction"])

    
@bp.route('/create_account', methods=('POST', ))
@login.login_required
def create_account():
    form = CreationForm(request.form)
    if form.validate_on_submit():
        compte = Compte()
        form.populate_obj(compte)
        compte.personne = login.current_user
        db.session.add(compte)
        db.session.commit()

    return redirect(url_for('banque.index'))


@bp.route('/delete_account', methods=('POST', ))
@login.login_required
def delete_account():

    form = DeletionForm(request.form)
    if form.validate_on_submit():
        db.session.query(Compte).filter(Compte.id ==form.compte_id.data).delete()
        db.session.commit()
        return redirect(url_for('banque.index'))
    return "fail",  400
    
    

