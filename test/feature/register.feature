Feature: Register
    A site where the user can register

    Scenario: User is registering
       Given: The user doesnt have an existing account on the platform.
       And: The user wants to register.
       When: The user inputs a non-existing account/email.
       And: The user presses the register button.
       Then: The user should register successfully.
