from behave import given, step
from helpers import validate_step_input


@step('admin logins to office')
def admin_logins_to_office(context):
    # init browser
    office_browser = context.BeeDriver()
    context.browsers['office']['first'] = office_browser

    # login to office
    office_po = office_browser.po.office
    office_po.load()
    office_config = office_browser.config.office
    email = office_config['login_name']
    password = office_config['login_password']
    office_browser.ac.office.login(email, password)
