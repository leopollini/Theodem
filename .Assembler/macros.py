import hashlib

DEBUG_MODE = True

def encode_string(str):
	asd = hashlib.md5()
	asd.update(str.encode())
	return asd.hexdigest()

def encode_json(obj):
	return encode_string(str(obj))

def sort_by_name_args_func(x):
	return str(x.name) + str(x.args)
