from flask_restful import Resource
from datetime import datetime

class BasicInfo(Resource):
    def get(self):
        return {
            'email': 'tettehmagnus35@gmail.com',
            'current_datetime': datetime.utcnow().isoformat(),
            'github_url': 'https://github.com/Magnus984/BasicAPI'
        }

class root(Resource):
    def get(self):
        return {
            'message': 'Welcome to the BasicAPI',
            'redirect_url': 'https://magnus984.pythonanywhere.com/api/v1/info'
        }