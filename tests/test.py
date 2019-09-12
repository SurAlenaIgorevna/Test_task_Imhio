from application import Application

def test_feedback_service(app:Application):
    i = 0
    for i in range (7, 11):
        app.Methods.open_homepage()
        app.Methods.delete_cookie()

        while len(app.driver.find_elements_by_class_name('NPS')) == 0:
            app.Methods.delete_cookie()

        app.driver.find_elements_by_class_name('NPS__button-container')[i].click()
        if i <= 6:
            app.Methods.fill_textarea('My feedback')
        else:
            assert len(app.driver.find_elements_by_class_name('NPS__feedback-textarea-container')) == 0, 'Поле открылось для оценки выше 7!'
        i +=1
