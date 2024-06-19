from selene import browser, have


def test_complete_todo():
    browser.open('/')
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
    browser.element('//div[contains(text(),"15")]').click()
    browser.element('#subjectsInput').type('co').press_enter()
    browser.element("//label[@for='hobbies-checkbox-1']").click()
    browser.element("#currentAddress").type("Moscow, Manoilov Street, 64")
    browser.element("#react-select-3-input").type("NCR").press_enter()
    browser.element("#react-select-4-input").type("Gurgaon").press_enter()
    browser.element('#submit').click()

    browser.element("#example-modal-sizes-title-lg").should(have.text('Thanks for submitting the form'))
    browser.element(".table-responsive").should(have.text('Alex'))
    browser.element(".table-responsive").should(have.text('Smirnov'))
    browser.element(".table-responsive").should(have.text('alex.smirnov@gmail.com'))
    browser.element(".table-responsive").should(have.text('Male'))
    browser.element(".table-responsive").should(have.text('5648798798'))
    browser.element(".table-responsive").should(have.text('15 May,2014'))
    browser.element(".table-responsive").should(have.text('Sports'))
    browser.element(".table-responsive").should(have.text('NCR Gurgaon'))
