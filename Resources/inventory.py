from flask_restful import Resource, reqparse
from Models.inventory import InventoryModel
from datetime import datetime

item_parser = reqparse.RequestParser()
item_parser.add_argument('category', type=str, required=True, help='This field cannot be left blank')
item_parser.add_argument('manufacturing_date', type=lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S'), required=True,
                         help='This field cannot be left blank')
item_parser.add_argument('expiry_date', type=lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S'), required=True,
                         help='This field cannot be left blank')
item_parser.add_argument('quantity', type=int, required=True, help='This field cannot be left blank')


class Inventory(Resource):
    def get(self, name):
        item = InventoryModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found.'}, 404

    def post(self, name):
        if InventoryModel.find_by_name(name):
            return {'message': 'Item already Exists.'}, 400

        data = item_parser.parse_args()
        item = InventoryModel(name, **data)
        try:
            item.save_to_db()
        except:
            return {'message': 'Error occur while inserting item.'}
        return item.json(), 201

    def put(self, name):
        data = item_parser.parse_args()
        item = InventoryModel.find_by_name(name)
        if item:
            item.category = data['category'],
            item.manufacturing_date = data['manufacturing_date'],
            item.expiry_date = data['expiry_date'],
            item.quantity = data['quantity']
        else:
            item = InventoryModel(name, **data)
        item.save_to_db()
        return item.json()

    def delete(self, name):
        item = InventoryModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {'message': 'Item Deleted'}
        else:
            return {'message': 'Item not found'}


class InventoryList(Resource):
    def get(self):
        items = [item.json() for item in InventoryModel.find_all()]
        return {'items': items}


# class InventorySearch(Resource):
#     def get(self, name):
#