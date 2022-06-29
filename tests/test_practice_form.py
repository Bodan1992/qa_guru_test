from selene.support.shared import browser
from selene import have, command
import os

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

    browser.element('#dateOfBirthInput').perform(command.js.scroll_into_view).click()
    browser.element('.react-datepicker__year-select').element('[value="1992"]').click()
    browser.element('.react-datepicker__month-select').element('[value="0"]').click()
    browser.element('.react-datepicker__day--001').click()

    browser.element('#subjectsInput').type('Maths').press_tab()
    browser.element('#subjectsInput').type('English').press_tab()

    browser.element('#hobbiesWrapper').all('.custom-checkbox').element_by(have.exact_text('Sports')).click()
    browser.element('#hobbiesWrapper').all('.custom-checkbox').element_by(have.exact_text('Music')).click()

    browser.element('#uploadPicture').send_keys(os.path.abspath('../resources/photo.jpg'))

    browser.element('#currentAddress').type('г.Киев, ул.Академика Туполева 20в')

    browser.element('#state').element('input').type('Haryana').press_tab()
    browser.element('#city').element('input').type('Karnal').press_tab()

    browser.element('#submit').perform(command.js.click)

    #Assert
    browser.element('.modal-dialog').element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    browser.element('.modal-dialog').all("table tr")[1].all('td').should(have.exact_texts('Student Name','Bohdan Obruch'))

    browser.element('.modal-dialog').all("table tr")[2].all('td').should(have.exact_texts('Student Email', 'bodan@gmail.com'))

    browser.element('.modal-dialog').all("table tr")[3].all('td').should(have.exact_texts('Gender', 'Male'))

    browser.element('.modal-dialog').all("table tr")[4].all('td').should(have.exact_texts('Mobile', '0960263611'))

    browser.element('.modal-dialog').all("table tr")[5].all('td').should(have.exact_texts('Date of Birth', '01 January,1992'))

    browser.element('.modal-dialog').all("table tr")[6].all('td').should(have.exact_texts('Subjects', 'Maths, English'))

    browser.element('.modal-dialog').all("table tr")[7].all('td').should(have.exact_texts('Hobbies','Sports, Music'))

    browser.element('.modal-dialog').all("table tr")[8].all('td').should(have.exact_texts('Picture', 'photo.jpg'))

    browser.element('.modal-dialog').all("table tr")[9].all('td').should(have.exact_texts('Address', 'г.Киев, ул.Академика Туполева 20в'))

    browser.element('.modal-dialog').all("table tr")[10].all('td').should(have.exact_texts('State and City', 'Haryana Karnal'))