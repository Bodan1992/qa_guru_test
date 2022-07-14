from selene.support.shared import browser
from selene import have, command

from demoqa_test.controls.dropdown import Dropdown
from demoqa_test.controls.table import Table
from demoqa_test.controls.tags_input import TagsInput
from demoqa_test.controls.utils import resource
from demoqa_test.controls.datepicker import DatePicker



def arrange_form_opened():
    browser.open('/automation-practice-form')
    browser.all(
        '[id^=google_ads][id$=container__]').with_(timeout=10).should(have.size(3)).perform(command.js.remove)


def test_register_form():
    arrange_form_opened()

    # Act
    browser.element('#firstName').type('Bohdan')

    browser.element('#lastName').type('Obruch')

    browser.element('#userEmail').type('bodan@gmail.com')

    gender_group = browser.element('#genterWrapper')
    gender_group.all('.custom-radio').element_by(have.exact_text("Male")).click()

    mobileNumber = browser.element('#userNumber')
    mobileNumber.type('0960263611')

    date_of_birth = DatePicker(browser.element('#dateOfBirthInput'))
    date_of_birth.select_year(1992)
    date_of_birth.select_month(0)
    date_of_birth.select_day(1)
    # date_of_birth.explicit_input('01 Jan 1992')

    subjects = TagsInput(browser.element('#subjectsInput'))
    subjects.add('Ma', autocomplete='Maths')
    subjects.add('English')

    browser.element('#hobbiesWrapper').all('.custom-checkbox').element_by(have.exact_text('Sports')).click()
    browser.element('#hobbiesWrapper').all('.custom-checkbox').element_by(have.exact_text('Music')).click()

    browser.element('#uploadPicture').send_keys(resource('photo.jpg'))

    browser.element('#currentAddress').type('г.Киев, ул.Академика Туполева 20в').perform(command.js.scroll_into_view)

    Dropdown(browser.element('#state')).select(option='Haryana')
    Dropdown(browser.element('#city')).autocomplete(option='Kar')

    browser.element('#submit').perform(command.js.click)

    #Assert
    browser.element('.modal-dialog').element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    results = Table(browser.element('.modal-dialog'))

    results.cells_of_row(0).should(have.exact_texts('Student Name', 'Bohdan Obruch'))
    results.cells_of_row(1).should(have.exact_texts('Student Email', 'bodan@gmail.com'))
    results.cells_of_row(2).should(have.exact_texts('Gender', 'Male'))
    results.cells_of_row(3).should(have.exact_texts('Mobile', '0960263611'))
    results.cells_of_row(4).should(have.exact_texts('Date of Birth', '01 January,1992'))
    results.cells_of_row(5).should(have.exact_texts('Subjects', 'Maths, English'))
    results.cells_of_row(6).should(have.exact_texts('Hobbies','Sports, Music'))
    results.cells_of_row(7).should(have.exact_texts('Picture', 'photo.jpg'))
    results.cells_of_row(8).should(have.exact_texts('Address', 'г.Киев, ул.Академика Туполева 20в'))
    results.cells_of_row(9).should(have.exact_texts('State and City', 'Haryana Karnal'))
