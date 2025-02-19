import requests

from services.general.helpers.base_helper import BaseHelper


class StudentHelper(BaseHelper):
    PREFIX_ENDPOINT = "/students"
    ROOT_ENDPOINT = f"{PREFIX_ENDPOINT}/"

    def get_students(self) -> requests.Response:
        response = self.api_utils.get(self.ROOT_ENDPOINT)
        return response

    def post_student(self, json: dict) -> requests.Response:
        response = self.api_utils.post(self.ROOT_ENDPOINT, json=json)
        return response

    def delete_student(self, student_id: int) -> requests.Response:
        response = self.api_utils.delete(self.ROOT_ENDPOINT + str(student_id))
        return response

    def get_student(self, student_id: int) -> requests.Response:
        response = self.api_utils.get(self.ROOT_ENDPOINT + str(student_id))
        return response

    def put_student(self, student_id: int, json: dict) -> requests.Response:
        response = self.api_utils.put(self.ROOT_ENDPOINT + str(student_id),
                                      json=json)
        return response
