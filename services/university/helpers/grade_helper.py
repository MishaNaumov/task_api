import requests

from services.general.helpers.base_helper import BaseHelper


class GradeHelper(BaseHelper):
    PREFIX_ENDPOINT = "/grades"
    ROOT_ENDPOINT = f"{PREFIX_ENDPOINT}/"
    STATS_ENDPOINT = f"{PREFIX_ENDPOINT}/stats/"

    def post_grade(self, data: dict) -> requests.Response:
        response = self.api_utils.post(self.ROOT_ENDPOINT, data=data)
        return response

    def get_grades(self) -> requests.Response:
        response = self.api_utils.get(self.ROOT_ENDPOINT)
        return response

    def delete_grade(self, grade_id: int) -> requests.Response:
        response = self.api_utils.delete(self.ROOT_ENDPOINT + str(grade_id))
        return response

    def put_grade(self, grade_id: int, data: dict) -> requests.Response:
        response = self.api_utils.put(self.ROOT_ENDPOINT + str(grade_id),
                                      data=data)
        return response

    def get_grades_stats(self, data: dict) -> requests.Response:
        response = self.api_utils.get(self.STATS_ENDPOINT, data=data)
        return response

