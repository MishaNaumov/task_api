class BaseService:
    SERVICE_URL = None

    def __init__(self, api_utils):
        self.api_utils = api_utils

