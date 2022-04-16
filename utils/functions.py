import secrets


def gen_key(length, charset="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"):
	return "".join([secrets.choice(charset) for _ in range(0, length)])

def gen_key_wa(length, charset="0123456789"):
	return "".join([secrets.choice(charset) for _ in range(0, length)])
