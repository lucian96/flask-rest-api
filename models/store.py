from db import db


class StoreModel(db.Model):
    """
    ORM - Object Relational Mapping
    This will be a mapping between table rows into a python object
    """
    __tablename__ = "stores"  # create a table named items

    id = db.Column(db.Integer, primary_key=True)  # defines a column in the above table, will be auto incremental
    name = db.Column(db.String(80), unique=True, nullable=False)
    items = db.relationship("ItemModel", back_populates="store", lazy="dynamic", cascade="all, delete")
