import hashlib

DEBUG_MODE = True

def encode_string(content) -> str:
	asd = hashlib.md5()
	asd.update(content.encode())
	return asd.hexdigest()

def encode_json(obj) -> str:
	return encode_string(str(obj))

def sort_by_name_args_func(x) -> str:
	return str(x.name) + str(x.args)
