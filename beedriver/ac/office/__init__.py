from beedriver.ac.action_chain import ActionChain

class OfficeAC(ActionChain):

    def login(self, email, password):
        office = self.client.po.office
        office.load()
        login_form = office.login_page.login_form
        login_form.email.set(email)
        login_form.password.set(password)
        login_form.submit_button.click()

