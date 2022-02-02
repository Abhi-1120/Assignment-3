from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from Resources.user import UserRegister, User
from Resources.inventory import Inventory, InventoryList, UpdateInventory

UPLOAD_FOLDER = 'C:/Users/agbha/PycharmProjects/Assignment-3/Inventory/image'

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/test_flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'Abhi'
api = Api(app)

jwt = JWT(app, authenticate, identity)


@app.before_first_request
def create_tables():
    if __name__ == '__main__':
        db.create_all()


api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(Inventory, '/inventory/<string:name>')
api.add_resource(UpdateInventory, '/inventory/<int:id>')
api.add_resource(InventoryList, '/inventory-list')

if __name__ == '__main__':
    from db import db

    db.init_app(app)
    app.debug = True
    app.run()
