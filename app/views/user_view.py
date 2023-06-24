from app.controllers.user_controller import UserController
from flask import Blueprint, render_template

user_bp = Blueprint('user', __name__)

@user_bp.route('/')
def index():
    return render_template('index.html')

@user_bp.route('/users', methods=['POST'])
def create_user():
    return UserController.create_user()

@user_bp.route('/users', methods=['GET'])
def get_users():
    return UserController.get_users()

@user_bp.route('/users',methods=['PUT'])
def update_user():
    return UserController.update_user()

@user_bp.route('/users',methods=['DELETE'])
def delete_user():
    return UserController.delete_user()