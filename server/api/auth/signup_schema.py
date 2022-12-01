from marshmallow import Schema, fields

class SignupSchema(Schema):
    email = fields.Str(required=True)
    password = fields.Str(required=True)