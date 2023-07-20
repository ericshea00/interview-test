from flask import Flask
from flask_restful import Api
from database import db
from resources import MessagesResource, NextMessageResource, MessageResource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
api = Api(app)

api.add_resource(MessagesResource, '/messages')
api.add_resource(MessageResource, '/message/<int:message_id>')
api.add_resource(NextMessageResource, '/next_message')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
