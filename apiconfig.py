from flask_restful import Api
from urls import Version1

# Config API urls
api = Api()
list(map(lambda x: api.add_resource(x[0], x[1]), Version1.urls))
