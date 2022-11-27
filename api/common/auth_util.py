import bcrypt
from Crypto.Hash import SHA256
from base64 import b64encode

class AuthUtil():
    def validate_user(user, password):

        # Create password hash
        try:
            b64pwd = b64encode(SHA256.new(password.encode('utf8')).digest())
        except:
            return False

        # Check password hash to see if it matches db
        try:
            if not bcrypt.checkpw(b64pwd, user.password.encode('utf8')):
                return "Bad Username or Password", 401
        except:
            return False
        
        return True
    
    def hash_password(password):
        # Create password hash
        try:
            b64pwd = b64encode(SHA256.new(password.encode('utf8')).digest())
        except:
            return False
        
        return b64pwd