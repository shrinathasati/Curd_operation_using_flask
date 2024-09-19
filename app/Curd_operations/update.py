from app import mongo
from app.models import user_schema, users_schema

class Update: 
    def update_user(self, user_id, data):
        mongo.db.users.update_one(
            {'id': user_id},
            {'$set': {
                'name': data['name'],
                'email': data['email'],
                'password': data['password']
            }}
        )
        user = mongo.db.users.find_one_or_404({"id": user_id})
        return user_schema.dump(user)