from app import app, api


@app.before_first_request
def create_tables():
    if __name__ == '__main__':
        db.create_all()


def add_routes(_api):
    from resources import UserRegister, User, Inventory, InventoryList, UpdateInventory

    _api.add_resource(UserRegister, '/register')
    _api.add_resource(User, '/user/<int:user_id>')
    _api.add_resource(Inventory, '/inventory/<string:name>')
    _api.add_resource(UpdateInventory, '/inventory/<string:name>')
    _api.add_resource(InventoryList, '/inventory-list')


if __name__ == '__main__':
    from db import db

    db.init_app(app)
    add_routes(api)
    app.debug = True
    app.run()
