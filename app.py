from flask import Flask
from flask_restful import Api
import logging

UPLOAD_FOLDER = 'C:/Users/agbha/PycharmProjects/Assignment-3/inventory/image/'

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/inventory'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'Abhi'
api = Api(app)


def configure_logger():
    logging.basicConfig(filename='logs.txt', level=logging.DEBUG,
                        format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
    return logging.getLogger(__name__)


logger = configure_logger()
