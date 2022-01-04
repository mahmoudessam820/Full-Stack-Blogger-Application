#-------------------------------------------------------------#
# Imports
#-------------------------------------------------------------#
import datetime
from sqlalchemy import (Column, String, Integer, create_engine)
from flask_sqlalchemy import SQLAlchemy


#-------------------------------------------------------------#
# Database config
#-------------------------------------------------------------#
user_name = 'postgres'
password = '1234'
host = 'localhost:5432'
database_name = 'blogger'
database_path = "postgres://{}:{}@{}/{}".format(
    user_name, password, host, database_name)

db = SQLAlchemy()

#---------------------------------------------------------------#
# setup_db(app)
# Binds a flask application and a SQLAlchemy service
#---------------------------------------------------------------#


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


#---------------------------------------------------------------#
# Model
#---------------------------------------------------------------#

class Articles(db.Model):
    __tablename__ = 'Articles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    art_body = db.Column(db.Text())
    date = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, title: str, art_body: str):
        self.title = title
        self.art_body = art_body

    def __repr__(self):
        return f"Article('{self.title}', '{self.art_body}', '{self.date}')"

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'body': self.art_body,
            'date': self.date
        }
