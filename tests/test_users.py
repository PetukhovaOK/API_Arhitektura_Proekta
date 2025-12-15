import allure

from config.base_test import BaseTest

@allure.epic("Users")
@allure.feature("Create_user")
class TestUsers(BaseTest):

    @allure.title("New user")
    def test_create_user(self):
        user = self.user_api.create_user()
        print(user.uuid)
