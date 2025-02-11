import requests

from services.general.helpers.base_helper import BaseHelper


class GroupHelper(BaseHelper):
    PREFIX_ENDPOINT = "/groups"
    ROOT_ENDPOINT = f"{PREFIX_ENDPOINT}/"

    def get_groups(self) -> requests.Response:
        response = self.api_utils.get(self.ROOT_ENDPOINT)
        return response

    def post_group(self, json: dict) -> requests.Response:
        response = self.api_utils.post(self.ROOT_ENDPOINT, json=json)
        return response

    def delete_group(self, group_id: int) -> requests.Response:
        response = self.api_utils.delete(self.ROOT_ENDPOINT + str(group_id))
        return response

    def get_group(self, group_id: int) -> requests.Response:
        response = self.api_utils.get(self.ROOT_ENDPOINT + str(group_id))
        return response

    def put_group(self, group_id: int, json: dict) -> requests.Response:
        response = self.api_utils.put(self.ROOT_ENDPOINT + str(group_id),
                                      json=json)
        return response
