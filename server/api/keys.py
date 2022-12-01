import os

JWT_SECRET = os.environ["JWT_SECRET"]

DB_CONFIG = {
    'DB_USER': os.environ["DB_USER"],
    'DB_PASS': os.environ["DB_PASS"],
    'DB_DOMAIN': os.environ["DB_DOMAIN"]
}