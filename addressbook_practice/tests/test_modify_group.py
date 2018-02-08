from model.group import *

def test_modify_group_name(app):
    app.session.login(username = 'admin', password = 'admin')
    app.group.modify_first_group(Group(name = 'New name'))
    app.session.logout()

#def test_modify_group_header(app):
#    app.session.login(username = 'admin', password = 'admin')
#    app.group.modify_first_group(Group(header = 'New header'))
#    app.session.logout()
