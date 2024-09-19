from app import mongo
from app.models import user_schema, users_schema

class Read:
    def get_user_by_id(self, user_id):
        user = mongo.db.users.find_one_or_404({"id": user_id})
        return user_schema.dump(user)