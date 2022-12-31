from db import db


class TagModel(db.Model):
    """
    ORM - Object Relational Mapping
    This will be a mapping between table rows into a python object
    """
    __tablename__ = "tags"  # create a table named tags

    id = db.Column(db.Integer, primary_key=True)  # defines a column in the above table, will be auto incremental
    name = db.Column(db.String(80), unique=True, nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), nullable=False)

    store = db.relationship("StoreModel", back_populates="tags")
    items = db.relationship("ItemModel", back_populates="tags", secondary="items_tags")

