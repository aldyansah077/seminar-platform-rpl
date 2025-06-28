from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email

class PendaftaranForm(FlaskForm):
    nama = StringField('Nama Lengkap', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    no_hp = StringField('No. HP', validators=[DataRequired()])
    seminar_id = SelectField('Pilih Seminar', coerce=int)
    submit = SubmitField('Daftar')