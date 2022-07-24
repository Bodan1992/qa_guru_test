from selene import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

from demoqa_test.data.data import *
from demoqa_test.controls.table import Table
from demoqa_test.pages.student_form_page import StudentRegistrationForm
from demoqa_test.controls.utils import arrange_form_opened


def test_submit_automation_practice_form():
    #Given
    arrange_form_opened()

    # When
    (
        StudentRegistrationForm()
        .set_first_name(Student.name)
        .set_last_name(Student.surname)
        .set_email(Student.email)
        .set_mobile_number(Student.mobile_number)
        .set_gender(Gender.male)
        .set_birth_date(Student.year,
                        Student.month,
                        Student.day)
        .select_subjects(Subjects.maths,
                         Subjects.english)
        .select_hobbies(Hobbies.music,
                        Hobbies.sports)
        .upload_picture(Student.avatar)
        .set_address(Student.address)
        .set_state_and_city(Student.state, Student.city)
    )

    StudentRegistrationForm().submit_form()

    # Then
    results = Table(s('.table'))
    (
        results
        .check_data(1, 1, Student.name,
                    Student.surname)
        .check_data(2, 1, Student.email)
        .check_data(3, 1, Gender.male)
        .check_data(4, 1, Student.mobile_number)
        .check_data(5, 1, Student.date_of_birth)
        .check_data(6, 1, Subjects.maths,
                    Subjects.english)
        .check_data(7, 1, Hobbies.music,
                    Hobbies.sports)
        .check_data(8, 1, Student.avatar)
        .check_data(9, 1, Student.address)
        .check_data(10, 1, Student.state, Student.city)
    )
