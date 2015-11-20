import mongoengine as db
from django.db import models

class BlogEntry(db.Document):
    title = db.StringField(max_length=50)
    content = db.StringField()
