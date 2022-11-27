from api.database import db

class AuthModel(db.Model):

    __tablename__ = "login"

    """
    Allowed data
    """
    uuid=db.Column(db.Integer, primary_key=True, autoincrement="auto")
    email = db.Column(db.String(255),nullable=False)
    password = db.Column(db.String(255),nullable=False)

    """
    Initialize model
    """
    def __init__(self, uuid, email, password):
        self.uuid = uuid
        self.email = email
        self.password = password

    ## TODO
    def find_by_email(email):
        return None

    ## TODO
    def update_token(email, token):
        return None
        

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()