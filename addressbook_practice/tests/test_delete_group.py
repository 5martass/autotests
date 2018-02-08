

def test_delete_first_group(app):
    app.session.login(username = 'admin', password = 'admin')
    app.group.delete_first_group()
    app.session.logout()
