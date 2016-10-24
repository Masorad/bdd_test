from behave import step
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


@step('feature "{featureId}" switch is "{state}"')
def feature_switch_is_state(context, featureId, state):
    valid_statuses = {'off', 'disabled', 'on', 'enabled'}
    validate_step_input(state, valid_statuses)

    try:
        office_browser = context.browsers['office']['first']
    except:
        context.execute_steps('Given admin logins to office')
        office_browser = context.browsers['office']['first']

    # navigate to features
    office_po = office_browser.po.office
    office_po.features.load()

    # ensure switch is in correct state
    desired_state = state in {'on', 'enabled'}
    office_po.tracy.close()  # necessary when browser is narrow
    office_po.features.ensure_feature_is_in_state(featureId, desired_state)
