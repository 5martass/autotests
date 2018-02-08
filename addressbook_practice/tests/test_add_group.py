from model.group import *

def test_add_group(app):
    app.group.create(Group(name = 'aaa', header = 'aaaa', footer = 'aaaaa'))
