from services.general.base_service import BaseService
from services.general.models.success_response import SuccessResponse
from services.university.helpers.grade_helper import GradeHelper
from services.university.helpers.group_helper import GroupHelper
from services.university.helpers.student_helper import StudentHelper
from services.university.helpers.teacher_helper import TeacherHelper
from services.university.models.grade.grade_request import GradeRequest
from services.university.models.grade.grade_response import GradeResponse
from services.university.models.grade.grade_statistic_response import \
    GradeStatisticResponse
from services.university.models.group.group_request import GroupRequest
from services.university.models.group.group_response import GroupResponse
from services.university.models.student.student_request import StudentRequest
from services.university.models.student.student_response import StudentResponse
from services.university.models.teacher.teacher_request import TeacherRequest
from services.university.models.teacher.teacher_response import TeacherResponse


class UniversityService(BaseService):
    SERVICE_URL = "http://127.0.0.1:8001"

    def __init__(self, api_utils):
        super().__init__(api_utils)

        self.group_helper = GroupHelper(api_utils)
        self.student_helper = StudentHelper(api_utils)
        self.teacher_helper = TeacherHelper(api_utils)
        self.grade_helper = GradeHelper(api_utils)

    def get_info_groups(self) -> SuccessResponse:
        response = self.group_helper.get_groups()
        return SuccessResponse(**response.json())

    def create_group(self, group_request: GroupRequest) -> GroupResponse:
        response = self.group_helper.post_group(
            json=group_request.model_dump())
        return GroupResponse(**response.json())

    def delete_group(self, group_id: int) -> SuccessResponse:
        response = self.group_helper.delete_group(group_id)
        return SuccessResponse(**response.json())

    def get_info_group(self, group_id: int) -> GroupResponse:
        response = self.group_helper.get_group(group_id)
        return GroupResponse(**response.json())

    def edit_group(self, group_id: int,
                   group_request: GroupRequest) -> GroupResponse:
        response = self.group_helper.put_group(group_id,
                                               json=group_request.model_dump())
        return GroupResponse(**response.json())

    def get_info_students(self) -> SuccessResponse:
        response = self.student_helper.get_students()
        return SuccessResponse(**response.json())

    def create_student(self,
                       student_request: StudentRequest) -> StudentResponse:
        response = self.student_helper.post_student(
            json=student_request.model_dump())
        return StudentResponse(**response.json())

    def delete_student(self, student_id: int) -> SuccessResponse:
        response = self.student_helper.delete_student(student_id)
        return SuccessResponse(**response.json())

    def get_info_student(self, student_id: int) -> StudentResponse:
        response = self.student_helper.get_student(student_id)
        return StudentResponse(**response.json())

    def edit_student(self, student_id: int,
                     student_request: StudentRequest) -> StudentResponse:
        response = self.student_helper.put_student(student_id,
                                                   json=student_request.model_dump())
        return StudentResponse(**response.json())

    def get_info_teachers(self) -> SuccessResponse:
        response = self.teacher_helper.get_teachers()
        return SuccessResponse(**response.json())

    def create_teacher(self,
                       teacher_request: TeacherRequest) -> TeacherResponse:
        response = self.teacher_helper.post_teacher(
            json=teacher_request.model_dump())
        return TeacherResponse(**response.json())

    def delete_teacher(self, teacher_id: int) -> SuccessResponse:
        response = self.teacher_helper.delete_teacher(teacher_id)
        return SuccessResponse(**response.json())

    def get_info_teacher(self, teacher_id: int) -> TeacherResponse:
        response = self.teacher_helper.get_teacher(teacher_id)
        return TeacherResponse(**response.json())

    def edit_teacher(self, teacher_id: int,
                     teacher_request: TeacherRequest) -> TeacherResponse:
        response = self.teacher_helper.put_teacher(teacher_id,
                                                   json=teacher_request.model_dump())
        return TeacherResponse(**response.json())

    def create_grade(self, grade_request: GradeRequest) -> GradeResponse:
        response = self.grade_helper.post_grade(
            data=grade_request.model_dump())
        return GradeResponse(**response.json())

    def get_info_grades(self) -> SuccessResponse:
        response = self.grade_helper.get_grades()
        return SuccessResponse(**response.json())

    def delete_grade(self, grade_id: int) -> SuccessResponse:
        response = self.grade_helper.delete_grade(grade_id)
        return SuccessResponse(**response.json())

    def edit_grade(self, grade_id: int,
                   grade_request: GradeRequest) -> GradeResponse:
        response = self.grade_helper.put_grade(grade_id,
                                               data=grade_request.model_dump())
        return GradeResponse(**response.json())

    # def get_grades_stats(self) -> GradeStatisticResponse:
    #     response = self.grade_helper.get_grades_stats(data=grade_statistic_response)
    #     return GradeStatisticResponse(**response.json())
