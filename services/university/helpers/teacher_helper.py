import requests

from services.general.helpers.base_helper import BaseHelper


class TeacherHelper(BaseHelper):
    PREFIX_ENDPOINT = "/teachers"
    ROOT_ENDPOINT = f"{PREFIX_ENDPOINT}/"

    def get_teachers(self) -> requests.Response:
        response = self.api_utils.get(self.ROOT_ENDPOINT)
        return response

    def post_teacher(self, json: dict) -> requests.Response:
        response = self.api_utils.post(self.ROOT_ENDPOINT, json=json)
        return response

    def delete_teacher(self, teacher_id: int) -> requests.Response:
        response = self.api_utils.delete(self.ROOT_ENDPOINT + str(teacher_id))
        return response

    def get_teacher(self, teacher_id: int) -> requests.Response:
        response = self.api_utils.get(self.ROOT_ENDPOINT + str(teacher_id))
        return response

    def put_teacher(self, teacher_id: int, json: dict) -> requests.Response:
        response = self.api_utils.put(self.ROOT_ENDPOINT + str(teacher_id),
                                      json=json)
        return response
