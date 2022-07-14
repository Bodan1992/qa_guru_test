from selene import command
from selene.core.entity import Element
from selene.support.shared import browser


class DatePicker:
    def __init__(self, element: Element):
        self.element = element

    def explicit_input(self, option: str):
        self.element.perform(command.js.set_value(option)).click()

    def select_year(self, option: int):
        self.element.click()
        browser.element('.react-datepicker__year-select').element(f'[value="{option}"]').click()

    def select_month(self, option: int):
        browser.element('.react-datepicker__month-select').element(f'[value="{option}"]').click()

    def select_day(self, option: int):
        browser.element(f'.react-datepicker__day--00{option}').click()
