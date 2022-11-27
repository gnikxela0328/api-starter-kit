from api.database import db

class UserModel(db.Model):

    __tablename__ = "users"

    # Allowed columns
    uuid = db.Column(db.String(36),primary_key=True)
    first_name = db.Column(db.String(255),nullable=False)
    last_name = db.Column(db.String(255),nullable=False)
    email = db.Column(db.String(255),nullable=False)
    password = db.Column(db.String(255),nullable=False)
    deleted = db.Column(db.Integer, nullable=True)
    #current_token = db.Column(db.String(311))

    # Initialize table

    def __init__(self, uuid, first_name, last_name, email, password, deleted):
        self.uuid = uuid
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.deleted = deleted
        

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()