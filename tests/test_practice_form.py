from selene.support.shared import browser
from selene import be, have, command

def opened_form():
    browser.open('/automation-practice-form')
    browser.all(
        '[id^=google_ads][id$=container__]').with_(timeout=10).should(have.size(3)).perform(command.js.remove)


def test_form():
    opened_form()
    # browser.open('/automation-practice-form')

    browser.element('#firstName').should(be.blank).type('Bohdan')
    browser.element('#lastName').should(be.blank).type('Obruch')
    browser.element('#userEmail').should(be.blank).type('bodan@gmail.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').should(be.blank).type('0960263611')
    browser.element('#dateOfBirthInput').scroll_to().click()
    browser.element('[value="1992"]').click()
    browser.element('[value="0"]').click()
    browser.element('div[aria-label="Choose Wednesday, January 1st, 1992"]').click()
    browser.element('#subjectsInput').should(be.blank).type('Maths').press_tab()
    browser.element('#subjectsInput').should(be.blank).type('English').press_tab()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').type('C:/Users/bohda/PycharmProjects/qa_guru-python/demoqa-test/tests/photo.jpg')
    browser.element('#currentAddress').should(be.blank).type('г.Киев, ул.Академика Туполева 20в')
    browser.element('#react-select-3-input').type('Haryana').press_tab()
    browser.element('#react-select-4-input').type('Karnal').press_tab().press_enter()
    #browser.element('#submit').click()

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.elements("table tr").element(1).should(have.text('Bohdan Obruch'))
    browser.elements("table tr").element(2).should(have.text('bodan@gmail.com'))
    browser.elements("table tr").element(3).should(have.text('Male'))
    browser.elements("table tr").element(4).should(have.text('0960263611'))
    browser.elements("table tr").element(5).should(have.text('01 January,1992'))
    browser.elements("table tr").element(6).should(have.text('Maths, English'))
    browser.elements("table tr").element(7).should(have.text('Sports, Music'))
    browser.elements("table tr").element(8).should(have.text('photo.jpg'))
    browser.elements("table tr").element(9).should(have.text('г.Киев, ул.Академика Туполева 20в'))
    browser.elements("table tr").element(10).should(have.text('Haryana Karnal'))

    # browser.elements('table tr').element(i).should(have.exact_texts(
    #     'Bohdan Obruch',
    #     'bodan@gmail.com',
    #     'Male',
    #     '0960263611',
    #     '01 January,1992',
    #     'Maths, English',
    #     'Sports, Music',
    #     'photo.jpg',
    #     'г.Киев, ул.Академика Туполева 20в',
    #     'Haryana Karnal'))

#scroll_to.
# .perform(command.js.scroll_into_view)

# browser.element('#uploadPicture').type('bohda\PycharmProjects\Automation_qa_guru\photo.jpg')