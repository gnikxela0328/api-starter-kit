from api.database import db

class ContactsModel(db.Model):

    __tablename__ = "contacts"

    # Allowed columns
    uuid = db.Column(db.String(36),primary_key=True)
    owner_uuid = db.Column(db.String(36),db.ForeignKey("auth.uuid"), nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    discord_username = db.Column(db.String(255))
    github_username = db.Column(db.String(255))
    twitter_username = db.Column(db.String(255))
    deleted = db.Column(db.Integer)

    # Initialize table

    def __init__(self, uuid, owner_uuid, first_name, last_name, email, discord_username, github_username, twitter_username, deleted):
        self.uuid = uuid
        self.owner_uuid = owner_uuid
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.discord_username = discord_username
        self.github_username = github_username
        self.twitter_username = twitter_username
        self.deleted = deleted
        
    def get_all_contacts(owner_uuid):
        contact_list = ContactsModel.query.filter_by(owner_uuid=owner_uuid).all()
        return contact_list
    

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()