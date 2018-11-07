import pytest

@pytest.fixture()
def setUp():
    print ('Setup before every method')
    yield
    print('Teardown after every method')

@pytest.fixture(scope='class')
def oneTimeSetup(request,browser,environment):
    print ('One Time etup before all methods')
    if browser == 'FF':
        amount = 10
        print (' we are using FF browser')
    else :
        amount = 20
        print('we are using IE browser')

    if request.cls is not None:
        request.cls.value = amount


    if environment == 'QA':
        print('we are using QA environment')
    if environment == 'QA2':
        print('we are using QA2 environment')

    yield amount
    print('One Time teardown after all methods')


def pytest_addoption(parser):
    parser.addoption('--browser')
    parser.addoption('--environment',help='provide with test environment to run in')

@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption('--browser')

@pytest.fixture(scope='session')
def environment(request):
    return request.config.getoption('--environment')



