from flask_restful import Resource
from datetime import datetime

class BasicInfo(Resource):
    def get(self):
        current_datetime = datetime.utcnow()
        formatted_datetime = current_datetime.replace(microsecond=0).isoformat() + "Z"
        return {
            'email': 'tettehmagnus35@gmail.com',
            'current_datetime': formatted_datetime,
            'github_url': 'https://github.com/Magnus984/BasicAPI'
        }

class root(Resource):
    def get(self):
        return {
            'message': 'Welcome to the BasicAPI',
            'redirect_url': 'https://magnus984.pythonanywhere.com/api/v1/info'
        }