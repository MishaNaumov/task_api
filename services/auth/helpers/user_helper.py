import requests

from services.general.helpers.base_helper import BaseHelper


class UserHelper(BaseHelper):
    PREFIX_ENDPOINT = "/users"
    ME_ENDPOINT = f"{PREFIX_ENDPOINT}/me/"

    def get_me(self) -> requests.Response:
        response = self.api_utils.get(self.ME_ENDPOINT)
        return response
