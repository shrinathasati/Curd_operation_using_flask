from app import mongo
from app.models import user_schema, users_schema

class AllUser:
    def get_all_users(self):
        users = mongo.db.users.find()
        return users_schema.dump(users)