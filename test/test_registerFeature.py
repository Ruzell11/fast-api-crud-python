from pytest_bdd import scenario, given, when, then
from controller.userController import createUser
from database.db import SessionLocal
from model.userModel import UserCreateSchema
from faker import Faker
import asyncio



is_click_the_register_submit_button = False
loop = asyncio.get_event_loop()
db_local = SessionLocal()
faker = Faker()
non_existent_email = faker.email()
first_name = faker.first_name()
last_name = faker.last_name()
password = faker.password()
response = None


scenario("./feature/register.feature", "User is registering")
def test_register():
    print("End of registering of user")
    pass

@given("The user doesn't have an existing account on the platform")
def test_given_user_does_not_have_existing_account():
    pass


@when("The user inputs a non-existing account/email.")
def test_user_inputs_non_existent_account():
    global response
    new_user = UserCreateSchema(
        email=non_existent_email,
        password=password,
        first_name=first_name,
        last_name=last_name,
    )
    response = loop.run_until_complete(createUser(db=db_local, user=new_user))
    pass


@then("The user should register successfully.")
def test_user_should_register_successfully():
    assert response["success"] is True
