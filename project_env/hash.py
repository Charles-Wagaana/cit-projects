import hashlib

password = "mynewpassword"

password = password.encode(encoding='UTF-8', errors='strict')

hashed_password = hashlib.sha512(password).hexdigest()

print(hashed_password)

