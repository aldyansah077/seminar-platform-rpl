from . import db

class Seminar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    judul = db.Column(db.String(100), nullable=False)
    deskripsi = db.Column(db.Text, nullable=False)
    tanggal = db.Column(db.Date, nullable=False)
    lokasi = db.Column(db.String(100), nullable=False)
    kuota = db.Column(db.Integer, nullable=False)
    pendaftar = db.relationship('Pendaftar', back_populates='seminar')

class Pendaftar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    no_hp = db.Column(db.String(20), nullable=False)
    seminar_id = db.Column(db.Integer, db.ForeignKey('seminar.id'), nullable=False)
    seminar = db.relationship('Seminar', back_populates='pendaftar')