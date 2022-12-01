from api.database import db

class AuthModel(db.Model):

    __tablename__ = "auth"

    """
    Allowed data
    """
    uuid=db.Column(db.String(36), primary_key=True, autoincrement="auto")
    email = db.Column(db.String(255),nullable=False)
    password = db.Column(db.String(255),nullable=False)
    current_token = db.Column(db.String(311))

    """
    Initialize model
    """
    def __init__(self, uuid, email, password, current_token):
        self.uuid = uuid
        self.email = email
        self.password = password
        self.current_token = current_token

    def find_by_email(email):
        user = AuthModel.query.filter_by(email=email).first()
        if user:
            return user
        else:
            return None
    
    def validate_token(user, token):
        if user.current_token == token:
            return True
        return False
    
    def lookup_token(token):
        user = AuthModel.query.filter_by(current_token=token).first()

        if user is None:
            return None
        else:
            return user.uuid

    def update_user_password(user, password):
        user.password = password
        db.session.commit()

    def update_token(user, token):
        user.current_token = token
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()