import decimal
from log import logger
from flask import json,request,redirect,url_for
import requests
import auth_util
import jwt

def response_fail_message(ret,errorMsg):
        return json.dumps({"ret":ret,"errorMsg":errorMsg,"data":""},cls=DecimalEncoder)

def response_success_data(data):
        return json.dumps({"ret":0,"errorMsg":"","data":data},cls=DecimalEncoder)


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)

def get_token_from_request(request):
	if not request:
		return None
	token = None
	tk_header = request.headers.get('Authorization')
	if tk_header:
		token = tk_header.split(" ")[1]
	return token

