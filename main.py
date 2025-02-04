import random

from faker import Faker
import requests

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


response_auth = requests.post(url=AUTH_URL + REGISTER_ENDPOINT,
                         data={
                             "username": user_name,
                             "password": password,
                             "password_repeat": password,
                             "email": faker.email()
                         })

response_login = requests.post(url=AUTH_URL + LOGIN_ENDPOINT,
                          data={
                              "username": user_name,
                              "password": password
                          })

token = response_login.json()["access_token"]
response_info = requests.get(url=AUTH_URL + GET_ME_ENDPOINT,
                         headers={
                             "Authorization": f"Bearer {token}"
                         })

response_group = requests.post(url=UNIVERSITY_URL + GROUPS_ENDPOINT,
                          json={
                              "name": faker.name()
                          },
                          headers={
                             "Authorization": f"Bearer {token}"
                          })
group_id = response_group.json()["id"]
response_student = requests.post(url=UNIVERSITY_URL + STUDENTS_ENDPOINT,
                          json={
                              "first_name": faker.first_name(),
                              "last_name": faker.last_name(),
                              "email": faker.email(),
                              "degree": random.choice(["Associate", "Bachelor",
                                                       "Master", "Doctorate"]),
                              "phone": faker.numerify("+7##########"),
                              "group_id": group_id
                          },
                          headers={
                              "Authorization": f"Bearer {token}"
                          })

print(response_student.status_code)
print(response_student.json())
