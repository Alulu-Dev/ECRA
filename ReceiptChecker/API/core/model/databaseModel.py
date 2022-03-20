from datetime import datetime

from flask_login import UserMixin
from mongoengine import *


class User(Document, UserMixin):
    code_name = StringField(required=True, unique=True, min_length=3)
    legal_name = StringField(required=True, max_length=50)
    password = StringField(required=True)
    data_created = DateTimeField(default=datetime.utcnow)
    status = StringField(required=True, default='Active', enumerate=['Active', 'Blocked', 'Deleted'])
    user_type = StringField(required=True, default='ECRA Operator', enumerate=['System', 'ECRA Operator', 'SuperAdmin'])

    meta = {
        'indexes': ['legal_name', 'user_type'],
        'ordering': ['user_type']
    }