from flask_restful import Resource, request
from user_model import UserModel
from user_schema import CreateUser, GetUser, UpdateUser, DeleteUser

create_schema = CreateUser()
get_schema = GetUser()
update_schema = UpdateUser()
delete_schema = DeleteUser()

class UserResource(Resource):

    # Place table get put post etc. here

    def sampleFunc(self):

        # args = request.args
        # err = schema.validate(args)
        # if (err):
        #     return "Incorrect Parameters Provided", 400

        print(self)

        # return "OK", 200

    def create_user(self):

        args = request.args
        err = create_schema.validate(args)
        if (err):
            return "Incorrect Parameters Provided", 400

        print(self)
        

        # return "OK", 200


    def sampleSave(self):

        # example = ExampleModel(args['first_name'],args['last_name'],args['email'],args['phone'],args['addresses'])
        # 
        # try:
        #     example.save_to_db()
        #     return "Example Updated", 200
        # except:
        #     return "Error saving to database", 403


        print(self)
    def sampleSave(self):

        # example = ExampleModel(args['first_name'],args['last_name'],args['email'],args['phone'],args['addresses'])
        # 
        # try:
        #     example.save_to_db()
        #     return "Example Updated", 200
        # except:
        #     return "Error saving to database", 403


        print(self)
    def sampleSave(self):

        # example = ExampleModel(args['first_name'],args['last_name'],args['email'],args['phone'],args['addresses'])
        # 
        # try:
        #     example.save_to_db()
        #     return "Example Updated", 200
        # except:
        #     return "Error saving to database", 403


        print(self)