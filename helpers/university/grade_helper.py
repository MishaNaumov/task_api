from helpers.base_helper import BaseHelper


class GradeHelper(BaseHelper):
    PREFIX_ENDPOINT = "/grades"
    ROOT_ENDPOINT = f"{PREFIX_ENDPOINT}/"
    STATS_ENDPOINT = f"{PREFIX_ENDPOINT}/stats/"

    def post_grade(self, data):
        response = self.api_utils.post(self.ROOT_ENDPOINT, data=data)
        return response

    def get_grades(self):
        response = self.api_utils.get(self.ROOT_ENDPOINT)
        return response

    def delete_grade(self, id_endpoint):
        response = self.api_utils.delete(self.ROOT_ENDPOINT + id_endpoint)
        return response

    def put_grade(self, id_endpoint, data):
        response = self.api_utils.put(self.ROOT_ENDPOINT + id_endpoint,
                                      data=data)
        return response

    def get_grades_stats(self, data):
        response = self.api_utils.get(self.STATS_ENDPOINT, data=data)
        return response

