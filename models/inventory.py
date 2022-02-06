from db import db
from datetime import datetime
from app import logger


class InventoryModel(db.Model):
    __tablename__ = 'inventory'
    logger.info('Creating a Table inventory.')
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    category = db.Column(db.String(80))
    manufacturing_date = db.Column(db.DateTime)
    expiry_date = db.Column(db.DateTime)
    quantity = db.Column(db.Integer)
    file = db.Column(db.String(80))
    timezone = db.Column(db.String(80))

    def __init__(self, name, category, manufacturing_date, expiry_date, quantity, file, timezone):
        logger.info('Initializing the objects Attributes.')
        self.name = name
        self.category = category
        self.manufacturing_date = manufacturing_date
        self.expiry_date = expiry_date
        self.quantity = quantity
        self.file = file
        self.timezone = timezone

    def json(self):
        logger.info('Display data in JSON format.')
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'manufacturing_date': self.manufacturing_date.strftime("%m-%d-%Y, %H:%M:%S"),
            'expiry_date': self.expiry_date.strftime("%m-%d-%Y, %H:%M:%S"),
            'quantity': self.quantity,
            'file': self.file,
            'timezone': self.timezone,
        }

    @classmethod
    def find_by_name(cls, name):
        logger.info('Finding inventory by there Name.')
        data = cls.query.filter_by(name=name).first()
        return data

    @classmethod
    def find_by_id(cls, _id):
        logger.info('Finding inventory by there ID.')
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls):
        logger.info('Display all inventory at a time.')
        return cls.query.all()

    def save_to_db(self):
        logger.info('Save inventory to the Database.')
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        logger.info('Deleting inventory from Database.')
        db.session.delete(self)
        db.session.commit()
