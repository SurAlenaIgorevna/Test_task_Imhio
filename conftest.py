import pytest
from application import Application

application = None

@pytest.fixture(scope='session', autouse=True)
def app(request):
    global application
    if application is None:
        application = Application()
    return application
