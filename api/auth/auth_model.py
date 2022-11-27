from api.database import db

class AuthModel(db.Model):

    __tablename__ = "login"

    """
    Sample Data
    """
    uuid=db.Column(db.Integer, primary_key=True, autoincrement="auto")
    email = db.Column(db.String(255),nullable=False)
    password = db.Column(db.String(255),nullable=False)

    """
    Sample Init
    """
    # def __init__(self, uuid, address, customer):
    #     self.uuid = uuid
    #     self.address = address
    #     self.customer = customer
        

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()