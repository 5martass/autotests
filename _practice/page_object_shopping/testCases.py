import pytest

@pytest.fixture
def test_cases(number):
    return testCases[number]


testCases = [
    #[severity, description]
    ['Blocker', 'when user goes to main page, page should be loaded'],
    ['Blocker', 'In Main page, when user search "Duck" button, he should see result for Duck'],
    ['Blocker', 'In Main page, when user click "Sing up" button, he should see Sign up Page'],
    ['Blocker', 'In Main page, when user click "Sing in" button, he should see Sign in Page'],
    ['Blocker', 'In Login Page, when user login with a valid user, he should see Home Page'],
    ['Blocker', 'In Login Page, when user login with a in-valid user, he should see Error Message'],
]
