# Core Dependencies
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_jwt_extended import JWTManager

# Utility
from api.database import db
from api.keys import DB_CONFIG, JWT_SECRET

# Resources
from api.auth.auth_resource import AuthResource
from api.auth.signup_resource import SignupResource
#from api.user.user_resource import UserResource


# Initialize app
app = Flask(__name__)
CORS(app)

## TODO
## Change this to postgres and include postgres into docker image
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://' + DB_CONFIG['DB_USER'] + ':' + DB_CONFIG['DB_PASS'] +'@' + DB_CONFIG['DB_DOMAIN'] 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["JWT_SECRET_KEY"] = JWT_SECRET


api = Api(app)
jwt = JWTManager(app)

db.init_app(app)

# Initialize database
@app.before_first_request
def create_tables():
    db.drop_all()
    db.create_all()

# Routes
api.add_resource(AuthResource, '/api/auth/')
api.add_resource(SignupResource, '/api/signup/')


if __name__ == '__main__':
    
    app.run(port=5000, debug=True, host='0.0.0.0')