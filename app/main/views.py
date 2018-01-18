# coding=utf-8
import decimal
from . import main
from flask import json,request
import postgresdb

@main.after_request
def apply_utf8(response):
	if "analyse" in request.url:
		response.headers['Content-Type']='application/json; charset=utf-8'
		response.headers['Access-Control-Allow-Origin'] = '*'
		response.headers['Access-Control-Allow-Headers'] = 'content-type,Content-Type'
		#response.headers['Access-Control-Allow-Credentials'] = 'true'
	return response

@main.route('/', methods=['GET', 'POST'])
def index():
	return 'index()'


def response_fail_message(ret,errorMsg):
	return json.dumps({"ret":ret,"errorMsg":errorMsg,"data":""},cls=DecimalEncoder)

def response_success_data(data):
	return json.dumps({"ret":0,"errorMsg":"","data":data},cls=DecimalEncoder)


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)

