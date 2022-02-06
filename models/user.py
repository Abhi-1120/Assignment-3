from db import db
from app import logger


class UserModel(db.Model):
    __tablename__ = 'users'
    logger.info('Creating a Table users.')
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def __init__(self, username, password):
        logger.info('Initializing the objects Attributes.')
        self.username = username
        self.password = password

    def json(self):
        logger.info('Display data in JSON format.')
        return {
            'id': self.id,
            'username': self.username
        }

    def save_to_db(self):
        logger.info('Save User to the Database.')
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        logger.info('Deleting User from Database.')
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, username):
        logger.info('Finding User by there Name.')
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        logger.info('Finding User by there ID.')
        return cls.query.filter_by(id=_id).first()
