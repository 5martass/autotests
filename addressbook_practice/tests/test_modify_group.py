from model.group import *

def test_modify_group_name(app):
    app.group.modify_first_group(Group(name = 'New name'))

def test_modify_group_header(app):
    app.group.modify_first_group(Group(header = 'New header'))
