from flask_restful import Resource, request
from flask_jwt_extended import create_access_token
import uuid

from api.common.auth_util import AuthUtil

from .auth_model import AuthModel
from .signup_schema import SignupSchema


class SignupResource(Resource):

    def __init__(self):
        self.schema = SignupSchema()

    """
    Sign up using email and password
    """
    def post(self):
        args = request.json
        err = self.schema.validate(args)
        if err:
            return "Incorrect Arguments", 400

        # Check for exisiting user
        user = AuthModel.find_by_email(args["email"])
        if user:
            return "Email is already in use", 401

        # Hash password
        password = AuthUtil.hash_password(args['password'])
        if not password:
            return {
                'message': "Error creating user"
            }, 401

        # Create uuid
        user_uuid = str(uuid.uuid4())

        # Create JWT Token
        jwt_token = create_access_token(identity=user_uuid)

        # Create user
        new_user = AuthModel(
            uuid=user_uuid, email=args['email'], password=password, current_token=jwt_token)

        # Save user
        try:
            new_user.save_to_db()
            return {
                'message': "New user created!"
            }, 201
        except:
            return {
                'message': "Error creating user"
            }, 403
