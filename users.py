users = [
    {
        "id": 1,
        "name": "Daniel Smith"
    }, {
        "id": 2,
        "name": "Ricky Martin"
    }, {
        "id": 3,
        "name": "Charlie Bond"
    }, {
        "id": 4,
        "name": "Douglas Nuth"
    }
]


def get_all_users():
    return users


def get_user(user_id):
    user_info = [user for user in users if user['id'] == user_id]
    return user_info
