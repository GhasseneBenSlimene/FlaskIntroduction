from bson import ObjectId
from app.models.user_model import User
from app.dto.user_dto import UserDTO
from app import db

class UserDAO:
    def create_user(self, user_dto):
        # Creating a User object from the UserDTO object
        user = User(user_dto.name, user_dto.lastname)
        # Inserting the User object into the database
        result = db.users.insert_one(user.__dict__)
        # Returning the inserted user's ID
        return str(result.inserted_id)

    def get_users(self):
        # Getting all the users from the database and converting them to UserDTO objects
        return [UserDTO(user) for user in db.users.find()]
    
    def update_user(self, user_dto):
        # Creating a User object from the UserDTO object
        user = User(user_dto.name, user_dto.lastname)
        # Updating the user in the database
        result = db.users.update_one({'_id': ObjectId(user_dto.id)}, {'$set': user.__dict__})
        # Returning the number of updated documents
        return result.modified_count

    def delete_user(self, user_dto):
        # Deleting the user from the database
        result = db.users.delete_one({'_id': ObjectId(user_dto.id)})
        # Returning the number of deleted documents
        return result.deleted_count
