# coding=utf-8
import jwt
import datetime
from log import logger

SECRET="my_darling"

def encode_auth_token(user_name):
	if not user_name or len(user_name) == 0:
		raise Exception("user_name is empty")
	try:
		payload = {
			'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7, seconds=5),
			'iat': datetime.datetime.utcnow(),
			'sub': user_name 
		}
		return jwt.encode(payload,SECRET,algorithm='HS256')
	except Exception as e:
		return e

def decode_auth_token(auth_token):
	if not auth_token or len(auth_token) == 0:
		raise Exception("auth_token is empty")
	try:
		payload = jwt.decode(auth_token, SECRET)
		return payload['sub']
	except jwt.ExpiredSignatureError:
		raise jwt.ExpiredSignatureError('Signature expired')
		return 'Signature expired. Please log in again.'
	except jwt.InvalidTokenError:
		raise jwt.InvalidTokenError('Invalid token')
		return 'Invalid token. Please log in again.'

logout_tokens = []
def logout_token(auth_token):
	global logout_tokens
	if auth_token:
		logout_tokens.append(auth_token)
	return

def is_token_logout(auth_token):
	if not auth_token:
		return True
	global logout_tokens
	if auth_token in logout_tokens:
		return True
	return False

if __name__ == '__main__':
	token = encode_auth_token("this is a name")
	print "token is %s"%token
	username = decode_auth_token(token)
	print "username %s"%username

