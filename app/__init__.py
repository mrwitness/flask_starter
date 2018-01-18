from flask import Flask

#Usage: app = create_app('default')
def create_app(config_name):
    app = Flask(__name__)
    app.config['SSL_DISABLE']=False

    if not app.debug and not app.testing and not app.config['SSL_DISABLE']:
#        from flask_sslify import SSLify
#        sslify = SSLify(app)
	pass

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
