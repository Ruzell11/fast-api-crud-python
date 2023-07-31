import unittest
import asyncio
from sqlalchemy.orm import Session
from model.userModel import UserCreateSchema , UserModel
from controller.userController import createUser, getSingleUserDetails , updateUserDetails
from faker import Faker
from database.db import SessionLocal
from fastapi import HTTPException
from unittest.mock import MagicMock
from constants.index import HTTP_CODE_OK , HTTP_CODE_NOT_FOUND


class UserUnitTesting(unittest.TestCase):
    def setUp(self):
        self.loop = asyncio.get_event_loop()
        self.db_mock = MagicMock(Session)
        self.db_local = SessionLocal()
        self.fake = Faker()
        self.email = self.fake.email()
        self.password = self.fake.password()
        self.first_name = self.fake.first_name()
        self.last_name = self.fake.last_name()
        self.user = UserCreateSchema(email=self.email, password=self.password , first_name=self.first_name , last_name=self.last_name)
        self.user_id_not_exist = 1000
        self.user_id_exist = 1

    def test_createUser(self):
        try:
            response = self.loop.run_until_complete(createUser(db=self.db_mock, user=self.user))
            self.assertEqual(response['success'], True)
        finally:
            self.db_mock.close()
            
    def test_getSingleUserDetailsNotExist(self):
        with self.assertRaises(HTTPException) as cm:
            self.loop.run_until_complete(getSingleUserDetails(db=self.db_local, user_id=self.user_id_not_exist))

        self.assertEqual(cm.exception.status_code, HTTP_CODE_NOT_FOUND)
        
    def test_getSingleUserDetailsExist(self):
        response = self.loop.run_until_complete(getSingleUserDetails(db=self.db_local , user_id=self.user_id_exist))

        self.assertEqual(response["success"], True)

    def test_updateUserDetailsUserNotExist(self):
       with self.assertRaises(HTTPException) as cm:
           self.loop.run_until_complete(updateUserDetails(db=self.db_local , user=self.user))
    
    # def test_updateUserDetailsExist(self):
    #     response = self.loop.run_until_complete(updateUserDetails(db=self.db_local , user=self.user))
       

    if __name__ == "__main__":
        unittest.main()
