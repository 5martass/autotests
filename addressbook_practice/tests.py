import pytest
from group import *
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.login(username = 'admin', password = 'admin')
    app.create_group(Group(name = 'aaa', header = 'aaaa', footer = 'aaaaa'))
    app.logout()
