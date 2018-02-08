import pytest
from model.group import *
from fixture.application import Application
from fixture.group import group_control

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.session.login(username = 'admin', password = 'admin')
    app.group.create(Group(name = 'aaa', header = 'aaaa', footer = 'aaaaa'))
    app.session.logout()
