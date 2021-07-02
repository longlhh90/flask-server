from flask_restful import Resource
from flask_jwt import current_identity, jwt_required


class Wow(Resource):

    @jwt_required()
    def get(self):
        return {"res": current_identity.email}
