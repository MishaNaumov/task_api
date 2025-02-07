from helpers.base_helper import BaseHelper


class AuthenticationHelper(BaseHelper):
    PREFIX_ENDPOINT = "/auth"

    REGISTER_ENDPOINT = f"{PREFIX_ENDPOINT}/register/"
    LOGIN_ENDPOINT = f"{PREFIX_ENDPOINT}/login/"

    def post_register(self, data):
        response = self.api_utils.post(self.REGISTER_ENDPOINT, data=data)
        return response

    def post_login(self, data):
        response = self.api_utils.post(self.LOGIN_ENDPOINT, data=data)
        return response
