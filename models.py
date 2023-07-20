from database import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_path = db.Column(db.String(255), unique=True, nullable=False)
    content = db.Column(db.String(500), nullable=False)
