from flask import Flask
from flask_restful import Api
from api.v1.routes.info import BasicInfo, root

app = Flask(__name__)
api = Api(app)
api.add_resource(root, '/')
api.add_resource(BasicInfo, '/api/v1/info')

if __name__ == '__main__':
    app.run(debug=True)