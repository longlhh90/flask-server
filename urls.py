from models.user import User
from api.student import Student
from api.user import UserRegister, Users


class Version1:
    list_path = [
        (Student, "students/<string:name>/"),
        (UserRegister, "sign-up/"),
        (Users, "users/")
    ]

    urls = list(map(lambda x: (x[0], "/api/v1/" + x[1]), list_path))
