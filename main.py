import random
from faker import Faker
from utils.api_utils import ApiUtils

faker = Faker()

AUTH_URL = "http://127.0.0.1:8000"
UNIVERSITY_URL = "http://127.0.0.1:8001"

REGISTER_ENDPOINT = "/auth/register/"
LOGIN_ENDPOINT = "/auth/login/"
GET_ME_ENDPOINT = "/users/me/"
GROUPS_ENDPOINT = "/groups/"
STUDENTS_ENDPOINT = "/students/"

user_name = faker.user_name()
password = faker.password()

anonym_auth_api_utils = ApiUtils(AUTH_URL)

response_auth = anonym_auth_api_utils.post(REGISTER_ENDPOINT,
                                           data={"username": user_name,
                                                 "password": password,
                                                 "password_repeat": password,
                                                 "email": faker.email()})

response_login = anonym_auth_api_utils.post(LOGIN_ENDPOINT,
                                            data={"username": user_name,
                                                  "password": password})

token = response_login.json()["access_token"]

response_info = anonym_auth_api_utils.get(
    GET_ME_ENDPOINT, headers={"Authorization": f"Bearer {token}"})

admin_university_api_utils = ApiUtils(
    UNIVERSITY_URL, headers={"Authorization": f"Bearer {token}"})


response_group = admin_university_api_utils.post(GROUPS_ENDPOINT,
                                                 json={"name": faker.name()})

group_id = response_group.json()["id"]

response_student = admin_university_api_utils.post(
    STUDENTS_ENDPOINT,
    json={"first_name": faker.first_name(),
          "last_name": faker.last_name(),
          "email": faker.email(),
          "degree": random.choice(["Associate", "Bachelor",
                                   "Master", "Doctorate"]),
          "phone": faker.numerify("+7##########"),
          "group_id": group_id}
)

print(response_info.status_code)
print(response_info.json())
