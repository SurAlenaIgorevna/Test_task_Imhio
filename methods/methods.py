class Methods():

    def __init__(self, app):
        self.app = app

    def open_homepage(self):
        driver = self.app.driver
        driver.get('http://localhost:58001/')

    def delete_cookie(self):
        driver = self.app.driver
        driver.delete_all_cookies()
        driver.refresh()

    def fill_textarea(self, feedback):
        driver = self.app.driver
        assert len(driver.find_elements_by_class_name('NPS__feedback-textarea-container')) == 1, 'Нет поля для комментария при оценке ниже 7!'
        driver.find_element_by_class_name('NPS__feedback-textarea').send_keys(feedback)
        driver.find_element_by_class_name('NPS__feedback-send').click()