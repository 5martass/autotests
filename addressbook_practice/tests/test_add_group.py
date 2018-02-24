from model.group import *

def test_add_group(app):
    app.group.create(Group(name = 'add name', header = 'add header', footer = 'add footer'))
