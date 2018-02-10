from model.group import *

def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name = 'qwe'))
    app.group.modify_first_group(Group(name = 'New name'))

def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header = 'qwe'))
    app.group.modify_first_group(Group(header = 'New header'))

def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(footer = 'qwe'))
    app.group.modify_first_group(Group(footer = 'New fooetr'))
