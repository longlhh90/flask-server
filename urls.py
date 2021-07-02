from models.user import User
from api.wow import Wow
from api.user import UserRegister, Users


class Version1:
    list_path = [
        (Wow, "wow/"),
        (UserRegister, "sign-up/"),
        (Users, "users/")
    ]

    urls = list(map(lambda x: (x[0], "/api/v1/" + x[1]), list_path))
