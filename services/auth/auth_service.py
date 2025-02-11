from services.auth.helpers.authentication_helper import AuthenticationHelper
from services.auth.helpers.user_helper import UserHelper
from services.auth.models.login_request import LoginRequest
from services.auth.models.login_response import LoginResponse
from services.auth.models.register_request import RegisterRequest
from services.auth.models.user_response import UserResponse
from services.general.base_service import BaseService
from services.general.models.success_response import SuccessResponse


class AuthService(BaseService):
    SERVICE_URL = "http://127.0.0.1:8000"

    def __init__(self, api_utils):
        super().__init__(api_utils)

        self.authentication_helper = AuthenticationHelper(api_utils)
        self.user_helper = UserHelper(api_utils)

    def register_user(self,
                      register_request: RegisterRequest) -> SuccessResponse:
        response = self.authentication_helper.post_register(
            data=register_request.model_dump())
        return SuccessResponse(**response.json())

    def login_user(self, login_request: LoginRequest) -> LoginResponse:
        response = self.authentication_helper.post_login(
            data=login_request.model_dump())
        return LoginResponse(**response.json())

    def get_me_info(self) -> UserResponse:
        response = self.user_helper.get_me()
        return UserResponse(**response.json())
