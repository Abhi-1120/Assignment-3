from db import db
from datetime import datetime


class InventoryModel(db.Model):
    __tablename__ = 'Inventory'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    category = db.Column(db.String(80))
    manufacturing_date = db.Column(db.DateTime)
    expiry_date = db.Column(db.DateTime)
    quantity = db.Column(db.Integer)

    def __init__(self, name, category, manufacturing_date, expiry_date, quantity):
        self.name = name
        self.category = category
        self.manufacturing_date = manufacturing_date
        self.expiry_date = expiry_date
        self.quantity = quantity

    def json(self):
        return {
            'name': self.name,
            'category': self.category,
            'manufacturing_date': self.manufacturing_date.isoformat(),
            'expiry_date': self.expiry_date.isoformat(),
            'quantity': self.quantity
        }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
