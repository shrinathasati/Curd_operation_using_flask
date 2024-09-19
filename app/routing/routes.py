from flask import Blueprint, request, jsonify
from app.Curd_operations.create import Create
from app.Curd_operations.read import Read
from app.Curd_operations.update import Update
from app.Curd_operations.delete import Delete
from app.Curd_operations.all_user import AllUser
# Define a blueprint for user-related routes
user_bp = Blueprint('users', __name__, url_prefix='/users')

# Initialize the user service
CreateUser = Create()
ReadUser = Read()
UpdateUser = Update()
DeleteUser = Delete()
all_user=AllUser()

@user_bp.route('/', methods=['GET'])
def get_users():
    users = all_user.get_all_users()
    return jsonify(users), 200

@user_bp.route('/<id>', methods=['GET'])
def get_user(id):
    user = ReadUser.get_user_by_id(id)
    return jsonify(user), 200

@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    user = CreateUser.create_user(data)
    return jsonify(user), 201

@user_bp.route('/<id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    user = UpdateUser.update_user(id, data)
    return jsonify(user), 200

@user_bp.route('/<id>', methods=['DELETE'])
def delete_user(id):
    DeleteUser.delete_user(id)
    return jsonify({"message": "User deleted successfully"}), 200
