from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ubah-dengan-key-aman'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///seminar.db'
    db.init_app(app)
    Bootstrap(app)

    from app.routes import main_bp
    app.register_blueprint(main_bp)

    with app.app_context():
        db.create_all()

    return app