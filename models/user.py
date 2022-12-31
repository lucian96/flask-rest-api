from db import db


class UserModel(db.Model):
    """
    ORM - Object Relational Mapping
    This will be a mapping between table rows into a python object
    """
    __tablename__ = "users"  # create a table named users

    id = db.Column(db.Integer, primary_key=True)  # defines a column in the above table, will be auto incremental
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
