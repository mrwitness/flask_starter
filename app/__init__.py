
from flask import Flask

#sqlite lib
#from flask_sqlalchemy import SQLAlchemy
#Todo: config...
#from config import config

#db = SQLAlchemy()

#Usage: app = create_app('default')
def create_app(config_name):
    app = Flask(__name__)
    app.config['SSL_DISABLE']=False

#currently comment out
#    app.config.from_object(config[config_name])
#    config[config_name].init_app(app)

#    db.init_app(app)

    if not app.debug and not app.testing and not app.config['SSL_DISABLE']:
#        from flask_sslify import SSLify
#        sslify = SSLify(app)
	pass

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
