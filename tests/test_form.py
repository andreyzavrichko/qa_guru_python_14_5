import os

from selene import browser, have


def test_complete_todo():
    browser.open('automation-practice-form/')
    browser.element('#firstName').type('Alex')
    browser.element('#lastName').type('Smirnov')
    browser.element('#userEmail').type('alex.smirnov@gmail.com')
    browser.element('.custom-control-label').click()
    browser.element('#userNumber').type('5648798798')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select').element(
        '[value="4"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select').element('[value="2014"]').click()
    browser.element('.react-datepicker__day--015').click()
    browser.element('#subjectsInput').type('co').press_enter()
    browser.element('[for=hobbies-checkbox-1]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('img.png'))
    browser.element("#currentAddress").type("Moscow, Manoilov Street, 64")
    browser.element("#react-select-3-input").type("NCR").press_enter()
    browser.element("#react-select-4-input").type("Gurgaon").press_enter()
    browser.element('#submit').click()
    browser.element("#example-modal-sizes-title-lg").should(have.text('Thanks for submitting the form'))
    browser.element('.table').all('td').even.should(have.exact_texts('Alex Smirnov',
                                                                     'alex.smirnov@gmail.com',
                                                                     'Male',
                                                                     '5648798798',
                                                                     '15 May,2014',
                                                                     'Computer Science',
                                                                     'Sports',
                                                                     'img.png',
                                                                     'Moscow, Manoilov Street, 64',
                                                                     'NCR Gurgaon'))

