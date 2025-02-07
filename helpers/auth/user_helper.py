from helpers.base_helper import BaseHelper


class UserHelper(BaseHelper):
    PREFIX_ENDPOINT = "/users"
    ME_ENDPOINT = f"{PREFIX_ENDPOINT}/me/"

    def get_me(self):
        response = self.api_utils.get(self.ME_ENDPOINT)
        return response
