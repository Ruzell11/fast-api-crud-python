import unittest
import asyncio
from sqlalchemy.orm import Session
from model.userModel import UserCreateSchema 
from controller.userController import createUser

from unittest.mock import MagicMock



class UserUnitTesting(unittest.TestCase):
    def setUp(self):
        self.email = "test+101@gmail.com"
        self.password = "12345"
        self.last_name = "Rivera"
        self.user = UserCreateSchema(email=self.email, password=self.password)

    def test_checkIfRequiredInputsIsPresent(self):
        self.assertIsNotNone(self.email)
        self.assertIsNotNone(self.password)

    def test_createUser(self):
        loop = asyncio.get_event_loop()
        db = MagicMock(Session)
        try:
            response = loop.run_until_complete(createUser(db=db, user=self.user))
            self.assertEqual(response["message"], "User created successfully")
        finally:
            db.close()


    if __name__ =='__main__':
        unittest.main()