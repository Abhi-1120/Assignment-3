from flask_restful import Resource, reqparse
from Models.user import UserModel
import logging


logging.basicConfig(filename='logs.txt', level=logging.DEBUG,
                    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
logger = logging.getLogger(__name__)


user_parser = reqparse.RequestParser()
user_parser.add_argument('username', type=str, required=True, help='This filed is required')
user_parser.add_argument('password', type=str, required=True, help='This filed is required')


class UserRegister(Resource):
    def post(self):
        logger.info('Register New Users to the database.')
        data = user_parser.parse_args()
        if UserModel.find_by_name(data['username']):
            logger.warning('User is Already Exists.')
            return {'message': 'User already Exist!'}, 400
        user = UserModel(**data)
        user.save_to_db()
        logger.info('User has been Successfully Created.')
        return {'message': 'User haas been created successfully'}, 201


class User(Resource):
    @classmethod
    def get(cls, user_id):
        logger.info('Searching for user by user_id.')
        user = UserModel.find_by_id(user_id)
        if user:
            logger.info('User Found.')
            return user.json()
        logger.error('User Not Found.')
        return {'message': 'User Not Found.'}

    @classmethod
    def delete(cls, user_id):
        logger.warning('Deleting User from Database.')
        user = UserModel.find_by_id(user_id)
        if user:
            logger.info('User get Deleted.')
            user.delete_from_db()
            return {'message': 'User has been deleted successfully.'}, 200
        logger.error('User Not Found.')
        return {'message': 'User Not Found.'}, 404
