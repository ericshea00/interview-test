from flask import request
from flask_restful import Resource
from db_service import DBService
from file_service import FileService


class MessagesResource(Resource):
    def post(self):
        message_content = request.json.get('message_content')
        if not message_content:
            return {'error': 'No message content provided'}, 400
        file_path = FileService.create_file(message_content)

        message_id = DBService.create_message(file_path, message_content)
        return {'id': message_id}, 201


class MessageResource(Resource):
    def get(self, message_id: int):
        message = DBService.get_message_by_id(message_id)
        content = FileService.get_file_content(message.file_path)
        return {'id': message_id, 'message_content': content}, 200

    def put(self, message_id: int):
        message_content = request.json.get('message_content')
        if not message_content:
            return {'error': 'No message content provided'}, 400
        # easier to delete the file and recreate
        message = DBService.get_message_by_id(message_id)
        FileService.delete_file(message.file_path)

        file_path = FileService.create_file(message_content)
        new_message_id = DBService.update_message(message, file_path, message_content)
        return {'id': new_message_id}, 200

    def delete(self, message_id: int):
        message = DBService.get_message_by_id(message_id)
        FileService.delete_file(message.file_path)
        DBService.delete_message(message)
        return {'id': message_id}, 200


class NextMessageResource(Resource):
    def get(self):
        message = DBService.get_recent_message()
        if not message:
            return {'error': 'No messages available'}, 404
        content = FileService.get_file_content(message.file_path)
        FileService.delete_file(message.file_path)
        DBService.delete_message(message)
        return {'id': message.id, 'message': content}, 200