from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
from . import auth     ## auth is a compatable solution between JAVA huoyan auth system.
#from ..models import Permission



#@main.app_context_processor
#def inject_permissions():
#    return dict(Permission=Permission)
