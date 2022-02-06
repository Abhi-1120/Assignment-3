from flask_restful import Resource, reqparse
from models.inventory import InventoryModel
from datetime import datetime
from flask import request
from dateutil import tz
from werkzeug.utils import secure_filename
import os
from common.utils import convert_date_into_cst
from app import logger

item_parser = reqparse.RequestParser()
item_parser.add_argument('category', type=str, required=True, help='This field cannot be left blank')
item_parser.add_argument('manufacturing_date', type=str, required=True, help='This field cannot be left blank')
item_parser.add_argument('expiry_date', type=str, required=True, help='This field cannot be left blank')
item_parser.add_argument('quantity', type=int, required=True, help='This field cannot be left blank')
item_parser.add_argument('file', location='files')
item_parser.add_argument('timezone', type=str)


class Inventory(Resource):
    def get(self, name):
        logger.info('Searching an inventory')
        item = InventoryModel.find_by_name(name)
        if item:
            return item.json()
        logger.error('Error occurred while Searching for inventory.')
        return {'message': 'Item not found.'}, 404

    def post(self, name):
        from app import app
        logger.info('Creating new inventory')
        if InventoryModel.find_by_name(name):
            return {'message': 'Item already Exists.'}, 400

        data = item_parser.parse_args()
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            url = os.path.relpath(file.filename)
            data['file'] = app.config['UPLOAD_FOLDER'] + url
            print(data)

        if 'timezone' in data:
            data['manufacturing_date'] = convert_date_into_cst(data['timezone'], data['manufacturing_date'])
            data['expiry_date'] = convert_date_into_cst(data['timezone'], data['expiry_date'])

        item = InventoryModel(name, **data)
        try:
            item.save_to_db()
        except Exception as e:
            logger.error('Error occurred while inserting an inventory.')
            return {'message': 'Error occur while inserting item.'}
        return item.json(), 201

    def delete(self, name):
        logger.warning('Deleting an inventory')
        item = InventoryModel.find_by_name(name)
        if item:
            item.delete_from_db()
            logger.info('inventory get Deleted Successfully.')
            return {'message': 'Item Deleted'}
        else:
            logger.error('Error occurred while deleting an inventory.')
            return {'message': 'Item not found'}


class UpdateInventory(Resource):
    def put(self, name):
        data = item_parser.parse_args()
        item = InventoryModel.find_by_name(name)
        if item:
            logger.info('Updating an inventory')
            item.category = data['category'],
            item.manufacturing_date = data['manufacturing_date'],
            item.expiry_date = data['expiry_date'],
            item.quantity = data['quantity']
        else:
            logger.info('Creating new inventory')
            item = InventoryModel(name, **data)
        item.save_to_db()
        return item.json()


class InventoryList(Resource):
    def get(self):
        logger.info('Display all Inventories.')
        items = [item.json() for item in InventoryModel.find_all()]
        return {'items': items}
