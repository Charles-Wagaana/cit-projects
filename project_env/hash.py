import hashlib

password = "mynewpassword"

hashed_password = hashlib.sha512().hexdigest()

print(hashed_password)

