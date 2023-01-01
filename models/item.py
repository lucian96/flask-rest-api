from db import db


class ItemModel(db.Model):
    """
    ORM - Object Relational Mapping
    This will be a mapping between table rows into a python object
    """
    __tablename__ = "items"  # create a table named items

    id = db.Column(db.Integer, primary_key=True)  # defines a column in the above table, will be auto incremental
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2), unique=False, nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), unique=False, nullable=False)
    # back_populates = property "items" from StoreModel(models.py -> StoreModel -> items(line 13))
    store = db.relationship("StoreModel", back_populates="items")
    tags = db.relationship("TagModel", back_populates="items", secondary="items_tags")


