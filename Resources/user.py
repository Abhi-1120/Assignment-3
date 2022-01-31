from flask_restful import Resource, reqparse
from Models.user import UserModel

user_parser = reqparse.RequestParser()
user_parser.add_argument('username', type=str, required=True, help='This filed is required')
user_parser.add_argument('password', type=str, required=True, help='This filed is required')


class UserRegister(Resource):

    def post(self):
        data = user_parser.parse_args()
        if UserModel.find_by_name(data['username']):
            return {'message': 'User already Exist!'}, 400

        user = UserModel(**data)
        user.save_to_db()
        return {'message': 'User haas been created successfully'}, 201


class User(Resource):
    @classmethod
    def get(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if user:
            return user.json()
        return {'message': 'User Not Found.'}

    @classmethod
    def delete(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if user:
            user.delete_from_db()
            return {'message': 'User has been deleted successfully.'}, 200
        return {'message': 'User Not Found.'}, 404
