import random

import requests.status_codes
from faker import Faker

from services.university.helpers.grade_helper import GradeHelper
from services.university.helpers.group_helper import GroupHelper
from services.university.helpers.teacher_helper import TeacherHelper

faker = Faker()


class TestGradeContract:
    def test_create_grade_with_group_id(self, university_api_utils_admin):
        group_helper = GroupHelper(university_api_utils_admin)
        group_response = group_helper.post_group(
            json={"name": faker.name()})

        teacher_helper = TeacherHelper(university_api_utils_admin)
        teacher_response = teacher_helper.post_teacher(json={
            "first_name": faker.first_name(),
            "last_name": faker.last_name(),
            "subject": random.choice(
                ["Mathematics", "Physics",
                 "History", "Biology", "Geography"])
        })

        grade_helper = GradeHelper(university_api_utils_admin)
        grade_response = grade_helper.post_grade(data={
            "teacher_id": teacher_response.json()["id"],
            "student_id": group_response.json()["id"],
            "grade": random.randint(0, 5)
        })

        assert grade_response.status_code == \
               requests.status_codes.codes.not_found, \
            f"Wrong status code. Actual: {group_response.status_code}," \
            f" but expected: {requests.status_codes.codes.not_found}"
