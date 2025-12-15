import allure
import requests

from services.users.payloads import Payloads
from config.headers import Headers
from services.users.endpoints import Endpoints
from utils.helper import Helper
from services.users.models.model_user import UserResponse


class UsersAPI(Helper):

    def __init__(self):
        self.payloads = Payloads()
        self.headers = Headers()
        self.endpoints = Endpoints()


    @allure.step("create user")
    def create_user(self) -> UserResponse:
        response = requests.post(
            url= self.endpoints.create_user,
            headers = self.headers.basic,
            json = self.payloads.create_user()
        )
        self.validate_response(response, UserResponse)