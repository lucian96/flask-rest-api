from db import db


class ItemTag(db.Model):
    """
    ORM - Object Relational Mapping
    This will be a mapping between table rows into a python object
    """
    __tablename__ = "items_tags"  # create a table named items_tags

    id = db.Column(db.Integer, primary_key=True)  # defines a column in the above table, will be auto incremental
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"))
    tag_id = db.Column(db.Integer, db.ForeignKey("tags.id"))
