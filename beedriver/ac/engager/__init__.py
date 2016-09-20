from beedriver.ac.action_chain import ActionChain


class EngagerAC(ActionChain):
    def login(self, email, password):
        engager = self.client.po.engager
        engager.load()
        login_form = engager.login_page.login_form
        login_form.email.set(email)
        login_form.password.set(password)
        login_form.submit_button.click()
