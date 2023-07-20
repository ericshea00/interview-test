import os
import uuid

FILE_EXTENSION = 'txt'
UPLOAD_FOLDER = 'messages'
# currently uses realtive path for folder
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

class FileService():

    @staticmethod
    def get_file_content(file_path):
        with open(file_path, 'r') as f:
            return f.read()

    @staticmethod
    def create_file(content):
        filename = f"{uuid.uuid4().hex}.{FILE_EXTENSION}"
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        with open(file_path, 'w') as f:
            f.write(content)
        return file_path

    @staticmethod
    def delete_file(file_path):
        os.remove(file_path)
