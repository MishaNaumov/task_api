from faker import Faker
import random

from services.university.models.group.group_request import GroupRequest
from services.university.models.student.base_student import DegreeEnum
from services.university.models.student.student_request import StudentRequest
from services.university.university_service import UniversityService

faker = Faker()


class TestStudentCreate:

    def test_create_student(self, university_api_utils_admin):
        university_service = UniversityService(university_api_utils_admin)
        group_request = GroupRequest(name=faker.name())
        group_response = university_service.create_group(group_request)

        group_id = group_response.id

        student_request = StudentRequest(first_name=faker.first_name(),
                                         last_name=faker.last_name(),
                                         email=faker.email(),
                                         degree=random.choice(
                                             [option for option in
                                              DegreeEnum]),
                                         phone=faker.numerify("+7##########"),
                                         group_id=group_id)
        student_response = university_service.create_student(student_request)
        student_group_id = student_response.group_id

        assert group_id == student_group_id,\
            f"Wrong group id. Actual: {student_group_id}," \
            f" but expected: {group_id}"
