# class User:
#     def __init__(self, username, password, phone=None):
#         self.username = username
#         self.password = password
#         self.phone = phone
#
#     def __str__(self):
#         return self.username
from datetime import datetime

from ext import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(12), nullable=False)
    phone = db.Column(db.String(11), unique=True)
    rdatetime = db.Column(db.DateTime, default=datetime.now)


    def __str__(self):
        return self.username
