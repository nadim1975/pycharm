import pytest

@pytest.mark.run(after='test_methodF')
def test_methodA(oneTimeSetup,setUp):
    print('running method A')

def test_methodB(oneTimeSetup,setUp):
    print ('running method B')

def test_methodC(oneTimeSetup,setUp):
    print ('running method C')

def test_methodD(oneTimeSetup,setUp):
    print ('running method D')

def test_methodE(oneTimeSetup,setUp):
    print ('running method E')


def test_methodF(oneTimeSetup,setUp):
    print ('running method F')