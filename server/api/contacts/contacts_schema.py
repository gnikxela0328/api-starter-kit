from marshmallow import Schema, fields

"""
Used to validate fields from incoming requests
"""

class CreateContact(Schema):
    first_name = fields.Str(required=False)
    last_name = fields.Str(required=False)
    email = fields.Str(required=False)
    discord_username = fields.Str(required=False)    
    github_username = fields.Str(required=False)
    twitter_username = fields.Str(required=False)   

class UpdateContact(CreateContact):
    uuid = fields.Str(required=True) 
    
