from flask_restful import Resource, reqparse
from models.user import User


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'email',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument(
        'password',
        type=str,
        required=True,
        help="This field cannot be blank."
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if User.find_by_email(data['email']):
            return {"message": "A user with that email already exists"}, 400

        user = User(data['email'], data['password'])
        user.save_to_db()

        return {"message": "User created successfully."}, 201


class Users(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'email',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument(
        'password',
        type=str,
        required=False,
        help="This field cannot be blank."
    )

    def get(self):
        data = Users.parser.parse_args()
        user = User.find_by_email(data['email'])
        return user.json()
