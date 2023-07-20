# from flask import request
from database import db
from models import Message


class DBService():
    @staticmethod
    def get_message_by_id(message_id):
        return db.session.query(Message).get(message_id)

    @staticmethod
    def get_recent_message():
        return db.session.query(Message).order_by(Message.id.asc()).first()

    @staticmethod
    def update_message(message, new_file_path, new_content):
        message.content = new_content
        message.file_path = new_file_path
        db.session.add(message)
        db.session.commit()
        return message.id

    @staticmethod
    def create_message(file_path, content):
        message = Message(file_path=file_path, content=content)
        db.session.add(message)
        db.session.commit()
        return message.id

    @staticmethod
    def delete_message(message):
         db.session.delete(message)
         db.session.commit()

