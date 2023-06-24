from flask import request, jsonify
from app.dao.user_dao import UserDAO
from app.dto.user_dto import UserDTO

class UserController:
    @staticmethod
    def create_user():
        # Creating a user object from the form data
        user_dto = UserDTO(request.form)
        # Inserting the user object into the database
        user_dao = UserDAO()
        user_id = user_dao.create_user(user_dto)
        # Returning a success response with the inserted user's ID
        return jsonify({'message': 'user created', 'id': user_id})

    @staticmethod
    def get_users():
        # Getting all the users from the database
        user_dao = UserDAO()
        users = user_dao.get_users()
        # Serializing the UserDTO objects
        serialized_users = [user.__dict__ for user in users]
        # Returning a success response with the serialized users
        return jsonify(serialized_users)
    
    @staticmethod
    def update_user():
        user_dao=UserDAO()
        user_dto=UserDTO(request.form)
        modified_count = user_dao.update_user(user_dto)
        # Returning a success response if the user was updated
        if modified_count==1:
            return jsonify({"message":"user updated"})
        # Returning a success response if there was nothing to update
        return jsonify({"message":"nothing to update"})
    
    @staticmethod
    def delete_user():
        user_dao=UserDAO()
        user_dto=UserDTO(request.form)
        deleted_count = user_dao.delete_user(user_dto)
        if deleted_count==1:
            return jsonify({"message":"user deleted"})
        # Returning a success response if the user does not exist
        return jsonify({"message":"user does not exist"})