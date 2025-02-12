import random

from faker import Faker

from services.university.models.grade.grade_request import GradeRequest
from services.university.models.group.group_request import GroupRequest
from services.university.models.student.base_student import DegreeEnum
from services.university.models.student.student_request import StudentRequest
from services.university.models.teacher.base_teacher import SubjectEnum
from services.university.models.teacher.teacher_request import TeacherRequest
from services.university.university_service import UniversityService

faker = Faker()


class TestGradeContract:
    def test_create_grade(self, university_api_utils_admin):
        university_service = UniversityService(university_api_utils_admin)
        group_request = GroupRequest(name=faker.name())
        group_response = university_service.create_group(group_request)

        student_request = StudentRequest(first_name=faker.first_name(),
                                         last_name=faker.last_name(),
                                         email=faker.email(),
                                         degree=random.choice(
                                             [option for option in
                                              DegreeEnum]),
                                         phone=faker.numerify("+7##########"),
                                         group_id=group_response.id)
        student_response = university_service.create_student(student_request)

        teacher_request = TeacherRequest(first_name=faker.first_name(),
                                         last_name=faker.last_name(),
                                         subject=random.choice(
                                             [option for option in
                                              SubjectEnum]))
        teacher_response = university_service.create_teacher(teacher_request)

        grade_request = GradeRequest(teacher_id=teacher_response.id,
                                     student_id=student_response.id,
                                     grade=random.randint(0, 5))
        grade_response = university_service.create_grade(grade_request)

        assert teacher_response.id == grade_response.teacher_id and\
               student_response.id == grade_response.student_id, \
            f"Wrong status code. Actual: {teacher_response.id} or" \
            f" {student_response.id}," \
            f" but expected: {grade_response.teacher_id} or" \
            f" {grade_response.student_id}"
