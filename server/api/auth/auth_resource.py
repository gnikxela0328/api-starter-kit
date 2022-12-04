from flask_restful import Resource, request
from flask_jwt_extended import create_access_token

from api.common.auth_util import AuthUtil

from .auth_model import AuthModel
from .auth_schema import AuthSchema

class AuthResource(Resource):

    def __init__(self):
        self.schema = AuthSchema()

    """
    Sign in using credentials
    """
    def post(self):
        args = request.json
        err = self.schema.validate(args)
        if err:
            print("bad args", flush=True)
            return "Incorrect Arguments", 400

        # Check for exisiting user
        user = AuthModel.find_by_email(args["email"])
        if user is None:
            return {
                'message': "Bad username or password"
            }, 401
        
        # Validate credentials
        if not AuthUtil.validate_user(user=user, password=args['password']):
            return {
                'message': "Bad username or password"
            }, 401

        # Password is good, Create JWT Token and update in db
        jwt_token = create_access_token(identity=user.uuid)
        AuthModel.update_token(user, jwt_token)

        return {
            'access_token': jwt_token,
        }, 201
        
        
    """
    Update existing credentials
    """
    def put(self):
        args = request.json
        err = self.schema.validate(args)
        if err:
            return "Incorrect Arguments", 400

        # Check for exisiting user
        user = AuthModel.find_by_email(args["email"])
        if user is None:
            return "Bad username or password", 401

        if request.headers["Authorization"] is None:
            return {
                'message': "Error authenticating"
            }, 400

        # Validate credentials
        if not AuthModel.validate_token(user=user, token=request.headers["Authorization"]):
            return {
                'message': "Error authenticating"
            }, 400

        # Hash new user password and update in db
        new_hash = AuthUtil.hash_password(args['password'])

        if new_hash is not None:
            AuthModel.update_user_password(user=user, password=new_hash)
        else:
            return {
                'message': "Error authenticating"
            }, 400

        # Password update succeeded, Create JWT Token and update in db
        jwt_token = create_access_token(identity=user.uuid)
        AuthModel.update_token(user, jwt_token)

        return {
            'access_token': jwt_token,
        }, 201