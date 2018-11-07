import pytest
from pytestpackage.classToTest import SomeClassToTest


@pytest.mark.usefixtures('oneTimeSetup','setUp') #to share the fixtures with all methods in the class
class Test_Reporting_Demo():

    @pytest.fixture(autouse=True)  #to share abc with other methods , created fixture and make it available to entire scope
    def classSetup(self,oneTimeSetup):
        self.abc = SomeClassToTest(self.value)

    def test_method1(self):
        results = self.abc.sumNumbers(5,6)
        assert results == 21
        print('running method 1')

    def test_method2(self):
        print('running method 2')
        results = self.abc.sumNumbers(5, 6)
        assert results > 20
