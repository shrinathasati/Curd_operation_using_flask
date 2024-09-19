from app import mongo
from app.models import user_schema, users_schema

class Create:
    def create_user(self, data):
        user = {
            'id': data['id'],
            'name': data['name'],
            'email': data['email'],
            'password': data['password']
        }
        mongo.db.users.insert_one(user)
        return user_schema.dump(user)