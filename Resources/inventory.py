from flask_restful import Resource, reqparse
from Models.inventory import InventoryModel
from datetime import datetime
from flask import request
import logging
from dateutil import tz
from werkzeug.utils import secure_filename
import os

logging.basicConfig(filename='logs.txt', level=logging.DEBUG,
                    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

logger = logging.getLogger(__name__)

item_parser = reqparse.RequestParser()
item_parser.add_argument('category', type=str, required=True, help='This field cannot be left blank')
item_parser.add_argument('manufacturing_date', type=str, required=True, help='This field cannot be left blank')
item_parser.add_argument('expiry_date', type=str, required=True, help='This field cannot be left blank')
item_parser.add_argument('quantity', type=int, required=True, help='This field cannot be left blank')
item_parser.add_argument('file', location='files')
item_parser.add_argument('timezone', type=str)


class Inventory(Resource):
    def get(self, name):
        logger.info('Searching an Inventory')
        item = InventoryModel.find_by_name(name)
        if item:
            return item.json()
        logger.error('Error occurred while Searching for Inventory.')
        return {'message': 'Item not found.'}, 404

    def post(self, name):
        from app import app
        logger.info('Creating new Inventory')
        if InventoryModel.find_by_name(name):
            return {'message': 'Item already Exists.'}, 400

        data = item_parser.parse_args()
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # if 'timezone' in data:
        #     data['manufacturing_date'] = convert_date_into_cst(data['timezone'], ['manufacturing_date'])
        #     data['expiry_date'] = convert_date_into_cst(data['timezone'], ['expiry_date'])

        dt_str = data['manufacturing_date']
        format = "%Y-%m-%d %H:%M:%S"

        local = datetime.strptime(dt_str, format)
        from_zone = tz.gettz(data['timezone'])
        to_zone = tz.gettz('UTC')
        local = local.replace(tzinfo=from_zone)
        central = local.astimezone(to_zone)
        dt_utc_str = central.strftime(format)

        central = datetime.strptime(dt_str, format)
        from_zone = tz.gettz('UTC')
        to_zone = tz.gettz(data['timezone'])
        central = central.replace(tzinfo=from_zone)
        data['manufacturing_date'] = central.astimezone(to_zone)

        dt_str = data['expiry_date']
        format = "%Y-%m-%d %H:%M:%S"

        local = datetime.strptime(dt_str, format)
        from_zone = tz.gettz(data['timezone'])
        to_zone = tz.gettz('UTC')
        local = local.replace(tzinfo=from_zone)
        central = local.astimezone(to_zone)
        dt_utc_str = central.strftime(format)

        central = datetime.strptime(dt_str, format)
        from_zone = tz.gettz('UTC')
        to_zone = tz.gettz(data['timezone'])
        central = central.replace(tzinfo=from_zone)
        data['expiry_date'] = central.astimezone(to_zone)

        item = InventoryModel(name, **data)
        try:
            item.save_to_db()
        except Exception as e:
            logger.error('Error occurred while inserting an Inventory.')
            return {'message': 'Error occur while inserting item.'}
        return item.json(), 201

    def delete(self, name):
        logger.warning('Deleting an Inventory')
        item = InventoryModel.find_by_name(name)
        if item:
            item.delete_from_db()
            logger.info('Inventory get Deleted Successfully.')
            return {'message': 'Item Deleted'}
        else:
            logger.error('Error occurred while deleting an Inventory.')
            return {'message': 'Item not found'}


class UpdateInventory(Resource):
    def put(self, id):
        data = item_parser.parse_args()
        item = InventoryModel.find_by_id(id)
        if item:
            logger.info('Updating an Inventory')
            item.category = data['category'],
            item.manufacturing_date = data['manufacturing_date'],
            item.expiry_date = data['expiry_date'],
            item.quantity = data['quantity']
        else:
            logger.info('Creating new Inventory')
            item = InventoryModel(id, **data)
        item.save_to_db()
        return item.json()


class InventoryList(Resource):
    def get(self):
        logger.info('Display all Inventories.')
        items = [item.json() for item in InventoryModel.find_all()]
        return {'items': items}
