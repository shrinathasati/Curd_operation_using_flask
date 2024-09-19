from app import mongo
from app.models import user_schema, users_schema

class Delete:
    def delete_user(self, user_id):
        mongo.db.users.delete_one({'id': user_id})