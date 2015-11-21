from django.test import TestCase

class NoDbTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def _fixture_setup(self):
        pass

    def _post_teardown(self):
        if self.available_apps is not None:
            print('Warning: Suppressed method that would signal apps about'+
                  ' changed settings.')

class TestFoo(NoDbTestCase):

    def test_bar(self):
        pass
