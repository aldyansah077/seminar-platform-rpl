from flask import Blueprint, render_template, redirect, url_for, flash
from .models import Seminar, Pendaftar
from .forms import PendaftaranForm
from . import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/seminars')
def seminar_list():
    seminars = Seminar.query.all()
    return render_template('seminar_list.html', seminars=seminars)

@main_bp.route('/daftar', methods=['GET', 'POST'])
def daftar():
    form = PendaftaranForm()
    form.seminar_id.choices = [(s.id, s.judul) for s in Seminar.query.all()]
    if form.validate_on_submit():
        peserta = Pendaftar(
            nama=form.nama.data,
            email=form.email.data,
            no_hp=form.no_hp.data,
            seminar_id=form.seminar_id.data
        )
        db.session.add(peserta)
        db.session.commit()
        flash('Pendaftaran berhasil!', 'success')
        return redirect(url_for('main.seminar_list'))
    return render_template('daftar.html', form=form)