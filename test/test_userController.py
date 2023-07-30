import unittest


class UserUnitTesting(unittest.TestCase):
    def setUp(self):
        self.email = False
        self.password = False

    def test_checkIfRequiredInputsIsPresent(self):
        self.assertIsNotNone(self.email)
        self.assertIsNotNone(self.password)
