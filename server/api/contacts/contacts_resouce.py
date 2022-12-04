import uuid
from flask_restful import Resource, request

from .contacts_model import ContactsModel
from .contacts_schema import CreateContact, UpdateContact
from api.auth.auth_model import AuthModel


class ContactsResource(Resource):

    def __init__(self):
        self.create_schema = CreateContact()
        self.update_schema = UpdateContact()


    """
    Create a new contact
    """
    def post(self):
        args = request.args
        err = self.create_schema.validate(args)
        if (err):
            return "Incorrect Parameters Provided", 400

        if "Authorization" in request.headers:
            user = AuthModel.lookup_token(request.headers['Authorization'])
            if user is not None:
                contact_uuid = str(uuid.uuid4())
                owner_uuid = user.uuid
                first_name = args["first_name"] if "first_name" in args else None
                last_name = args["last_name"] if "last_name" in args else None
                email = args["email"] if "email" in args else None
                discord_username = args["discord_username"] if "discord_username" in args else None
                github_username = args["github_username"] if "github_username" in args else None
                twitter_username = args["twitter_username"] if "twitter_username" in args else None
                deleted = 0

                try:
                    new_contact = AuthModel(uuid=contact_uuid, owner_uuid=owner_uuid, first_name=first_name, 
                    last_name=last_name, email=email, discord_username=discord_username, 
                    github_username=github_username, twitter_username=twitter_username)

                    new_contact.save_to_db()
                except:
                   return {
                    "message": "Error creating contact"
                }, 400 
            else:
                return {
                    "message": "Unauthorized"
                }, 400    
        else:
            return {
                "message": "Unauthorized"
            }, 400

        return {
                "message": "Contact created"
            }, 201


    """
    Get all contacts
    """
    def get(self):
        contacts = []
        if "Authorization" in request.headers:
            user = AuthModel.lookup_token(request.headers['Authorization'])
            if user is not None:
                contact_list = ContactsModel.get_all_contacts(owner_uuid=user.uuid)
            else:
                return {
                    "message": "Unauthorized"
                }, 400    
        else:
            return {
                "message": "Unauthorized"
            }, 400

        return {
                contacts
            }, 200

    def put(self):
        args = request.args
        err = self.update_schema.validate(args)
        if (err):
            return "Incorrect Parameters Provided", 400

        if "Authorization" in request.headers:
            user = AuthModel.lookup_token(request.headers['Authorization'])
            if user is not None:
                contact = ContactsModel.find_by_uuid(args["uuid"])

                if contact is not None:
                    contact.first_name = args["first_name"] if "first_name" in args else contact.first_name
                    contact.last_name = args["last_name"] if "last_name" in args else contact.last_name
                    contact.email = args["email"] if "email" in args else contact.email
                    contact.discord_username = args["discord_username"] if "discord_username" in args else contact.discord_username
                    contact.github_username = args["github_username"] if "github_username" in args else contact.github_username
                    contact.twitter_username = args["twitter_username"] if "twitter_username" in args else contact.twitter_username

                    try:
                        contact.save_to_db()
                    except:
                        return {
                        "message": "Error updating contact"
                        }, 401   
                else: 
                    return {
                        "message": "Contact not found"
                    }, 401
            else:
                return {
                    "message": "Unauthorized"
                }, 400    
        else:
            return {
                "message": "Unauthorized"
            }, 400

        return {
            "message": "Contact successfully updated"
        }, 200
    
    def delete(self):
        if "Authorization" in request.headers:
            user = AuthModel.lookup_token(request.headers['Authorization'])
            if user is not None:
                contact = ContactsModel.prepare_for_delete(owner_uuid=user.uuid, contact_uuid="")
            else:
                return {
                    "message": "Unauthorized"
                }, 400    
        else:
            return {
                "message": "Unauthorized"
            }, 400

        return {
                contacts
            }, 200
