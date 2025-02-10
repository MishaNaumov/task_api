from helpers.base_helper import BaseHelper


class TeacherHelper(BaseHelper):
    PREFIX_ENDPOINT = "/teachers"
    ROOT_ENDPOINT = f"{PREFIX_ENDPOINT}/"

    def get_teachers(self):
        response = self.api_utils.get(self.ROOT_ENDPOINT)
        return response

    def post_teacher(self, json):
        response = self.api_utils.post(self.ROOT_ENDPOINT, json=json)
        return response

    def delete_teacher(self, id_endpoint):
        response = self.api_utils.delete(self.ROOT_ENDPOINT + id_endpoint)
        return response

    def get_teacher(self, id_endpoint):
        response = self.api_utils.get(self.ROOT_ENDPOINT + id_endpoint)
        return response

    def put_teacher(self, id_endpoint, json):
        response = self.api_utils.put(self.ROOT_ENDPOINT + id_endpoint,
                                      json=json)
        return response
