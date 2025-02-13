from selene import browser, be, have

def test_search_results(open_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('html').should(have.text('yashaka/selene'))
    browser.quit()

def test_search_results_not_found(open_browser):
    browser.element('[name="q"]').should(be.blank).clear().type('xcbxciubo7545cbxcbuxcfbc7x6rb45xc55b4cx85g48xc54b8654dsvgsdfgvdfsgvb768#$%^&* ').press_enter()
    browser.element('html').should(have.text('результаты не найдены'))
    browser.quit()