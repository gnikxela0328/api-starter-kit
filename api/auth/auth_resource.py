from flask_restful import Resource, request
from flask_jwt_extended import create_access_token

from api.common.auth_util import AuthUtil

from .auth_model import AuthModel
from .auth_schema import AuthSchema

schema = AuthSchema()

class AuthResource(Resource):

    """
    Sign in using credentials
    """
    def post(self):
        args = request.json
        err = schema.validate(args)
        if err:
            return "Incorrect Arguments", 400

        # Check for exisiting user
        user = AuthModel.find_by_email(args["email"])
        if user is None:
            return "Bad username or password", 401
        
        # Validate credentials
        if not AuthUtil.validate_user(user=user, password=args['password']):
            return {
                'message': "Error authenticating"
            }, 400

        # Password is good, Create JWT Token and update in db
        jwt_token = create_access_token(identity=user.uuid)
        AuthModel.update_token(user, jwt_token)

        return {
            'access_token': jwt_token,
        }, 201
        

    ## TODO
    # Finish this...
    """
    Update existing credentials
    """
    def put(self):
        args = request.json
        err = schema.validate(args)
        if err:
            return "Incorrect Arguments", 400

        # Check for exisiting user
        user = AuthModel.find_by_email(args["email"])
        if user is None:
            return "Bad username or password", 401

        # Validate credentials
        if not AuthUtil.validate_user(user=user, password=args['password']):
            return {
                'message': "Error authenticating"
            }, 400

        # Hash new user password and update in db
        new_hash = AuthUtil.hash_password(args['password'])

        if new_hash is not None:
            AuthModel.update_user(new_hash)
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