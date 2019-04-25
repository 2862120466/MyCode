''' switch_collection上下文管理器允许您更改给定类的集合，允许跨集合快速方便地访问相同的组文档: '''

from mongoengine import connect, Document, StringField
from mongoengine.context_managers import switch_collection

connect('runoob')

class Group(Document):
    name = StringField()

Group(name='test').save()  # Saves in the default db

with switch_collection(Group, 'group') as Group:
    Group(name='hello Group 2000 collection!').save()  # Saves in group2000 collection