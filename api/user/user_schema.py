from marshmallow import Schema, fields

"""
Used to validate fields from incoming requests
"""

class CreateUser(Schema):
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True)

class GetUser(Schema):
    email = fields.Str(required=True)
    password = fields.Str(required=True)

class UpdateUser(Schema):
    first_name = fields.Str(required=False)
    last_name = fields.Str(required=False)
    email = fields.Str(required=False)
    password = fields.Str(required=False)
    
class DeleteUser(Schema):
    uuid = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True)
