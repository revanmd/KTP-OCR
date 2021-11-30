from flask import Flask
from flask_cors import CORS

def init_app(config_name):
	app = Flask(__name__,instance_relative_config=False)
	app.config.from_object(config_name)

	with app.app_context():
		from .api import api
		from .base import base
		
		app.register_blueprint(api, url_prefix='/v1')
		app.register_blueprint(base, url_prefix='/')

		CORS(app)

		return app
