from behave import given, when, then, step
from helpers import validate_step_input

@given('brand is {status} for chat')
def brand_is_status_for_chat(context, status):
    valid_statuses = {'offline', 'online'}
    validate_step_input(status, valid_statuses)

    # init browser
    engager_browser = context.BeeDriver(**context.browser_config)
    context.browsers['engager']['first'] = engager_browser
    engager_browser.po.engager.load()
    agent = engager_browser.config.agent
    engager_browser.ac.engager.login(agent['login'], agent['password'])

    # change status
    context.execute_steps(
        "When brand goes {} for chat".format(status))


@step('brand goes {status} for chat')
def brand_goes_status_for_chat(context, status):
    valid_statuses = {'offline', 'online'}
    validate_step_input(status, valid_statuses)

    engager = context.browsers['engager']['first'].po.engager
    desired_status = True if status == 'online' else False
    if not desired_status == engager.left_panel.livechat_button.is_online():
        engager.left_panel.livechat_button.click()


@step('agent opens {index} browser')
def agent_opens_second_browser(context, index):
    valid_indexes = {'first', 'second', 'third'}
    validate_step_input(index, valid_indexes)

    engager_browser = context.BeeDriver(**context.browser_config)
    context.browsers['engager'][index] = engager_browser
    engager_browser.po.engager.load()
    agent = engager_browser.config.agent
    engager_browser.ac.engager.login(agent['login'], agent['password'])


@then('agent should be {status} for chat in {index} browser')
def agent_should_be_status_in_index_browser(context, status, index):
    valid_indexes = {'first', 'second', 'third'}
    validate_step_input(index, valid_indexes)

    valid_statuses = {'offline', 'online'}
    validate_step_input(status, valid_statuses)

    engager = context.browsers['engager'][index].po.engager
    desired_status = True if status == 'online' else False
    assert engager.left_panel.livechat_button.is_online() == desired_status

