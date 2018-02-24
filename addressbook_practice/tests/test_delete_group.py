from model.group import *

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name = 'create new group del'))
    app.group.delete_first_group()
