import random

from faker import Faker

from helpers.auth.authentication_helper import AuthenticationHelper
from helpers.auth.user_helper import UserHelper
from helpers.university.group_helper import GroupHelper
from helpers.university.student_helper import StudentHelper
from utils.api_utils import ApiUtils

faker = Faker()

AUTH_URL = "http://127.0.0.1:8000"
UNIVERSITY_URL = "http://127.0.0.1:8001"

user_name = faker.user_name()
password = faker.password()

auth_helper = AuthenticationHelper(ApiUtils(AUTH_URL))
response_auth1 = auth_helper.post_register(data={"username": user_name,
                                                 "password": password,
                                                 "password_repeat": password,
                                                 "email": faker.email()})

response_login = auth_helper.post_login(data={"username": user_name,
                                              "password": password})

token = response_login.json()["access_token"]

user_helper = UserHelper(ApiUtils(
    AUTH_URL, headers={"Authorization": f"Bearer {token}"}))
response_temp = user_helper.get_me()

admin_university_api_utils = ApiUtils(
    UNIVERSITY_URL, headers={"Authorization": f"Bearer {token}"})

group_helper = GroupHelper(admin_university_api_utils)

response_group = group_helper.post_groups(json={"name": faker.name()})
response_group_2 = group_helper.get_groups()

group_id = response_group.json()["id"]

student_helper = StudentHelper(admin_university_api_utils)
response_student = student_helper.post_students(
    json={"first_name": faker.first_name(),
          "last_name": faker.last_name(),
          "email": faker.email(),
          "degree": random.choice(["Associate", "Bachelor",
                                   "Master", "Doctorate"]),
          "phone": faker.numerify("+7##########"),
          "group_id": group_id})
response_student_2 = student_helper.get_students()
