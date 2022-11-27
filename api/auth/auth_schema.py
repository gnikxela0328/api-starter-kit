from marshmallow import Schema, fields

class AuthSchema(Schema):
    email = fields.Str(required=True)
    password = fields.Str(required=True)