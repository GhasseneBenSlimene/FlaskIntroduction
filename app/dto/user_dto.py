class UserDTO:
    def __init__(self, data):
        self.id = str(data.get('_id'))
        self.name = data.get('name')
        self.lastname = data.get('lastname')