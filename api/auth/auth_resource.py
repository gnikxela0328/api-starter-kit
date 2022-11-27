from flask_restful import Resource, request
from flask_jwt_extended import create_access_token
import bcrypt
from Crypto.Hash import SHA256
from base64 import b64encode

from auth_model import AuthModel
from auth_schema import AuthSchema

schema = AuthSchema()

class AuthResource(Resource):

    # Sign in or Create new credentials
    def post(self):
        args = request.json
        err = authSchema.validate(args)
        if (err):
            return "Incorrect Arguments", 400


    def sampleSave(self):

        # example = ExampleModel(args['first_name'],args['last_name'],args['email'],args['phone'],args['addresses'])
        # 
        # try:
        #     example.save_to_db()
        #     return "Example Updated", 200
        # except:
        #     return "Error saving to database", 403


        print(self)