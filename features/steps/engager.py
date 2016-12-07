from behave import given, then, step
from helpers import validate_step_input


@given('brand is "{status}" for chat')
def brand_is_status_for_chat(context, status):
    valid_statuses = {'offline', 'online'}
    validate_step_input(status, valid_statuses)

    context.execute_steps('Given user is logged into engager')
    context.execute_steps('When "agent" waits for "2" seconds')
    context.execute_steps('When brand goes "{}" for chat'.format(status))


@step('brand goes "{status}" for chat')
def brand_goes_status_for_chat(context, status):
    valid_statuses = {'offline', 'online'}
    validate_step_input(status, valid_statuses)

    engager = context.browsers['engager']['first'].po.engager
    desired_status = status == 'online'
    if desired_status != engager.left_panel.livechat_button.is_online():
        engager.left_panel.livechat_button.click()


@step('agent opens "{index}" browser')
def agent_opens_second_browser(context, index):
    valid_indexes = {'first', 'second', 'third'}
    validate_step_input(index, valid_indexes)

    engager_browser = context.BeeDriver()
    context.browsers['engager'][index] = engager_browser
    engager_browser.po.engager.load()
    agent = engager_browser.config.agent
    engager_browser.ac.engager.login(agent['login'], agent['password'])


@step('agent refreshes engager browser')
def agent_refreshes_engager_browser(context):
    engager_browser = context.browsers['engager']['first']
    engager_browser.refresh()


@then('agent should be "{status}" for chat in "{index}" browser')
def agent_should_be_status_in_index_browser(context, status, index):
    valid_indexes = {'first', 'second', 'third'}
    validate_step_input(index, valid_indexes)

    valid_statuses = {'offline', 'online'}
    validate_step_input(status, valid_statuses)

    engager = context.browsers['engager'][index].po.engager
    desired_status = status == 'online'
    assert engager.left_panel.livechat_button.is_online() == desired_status


@then('livechat button is missing')
def livechat_button_is_missing(context):
    engager = context.browsers['engager']['first'].po.engager
    assert engager.left_panel.livechat_button.is_existing() is False


@given('user is logged into engager')
def user_is_logged_into_enagger(context):
    engager_browser = context.BeeDriver()
    context.browsers['engager']['first'] = engager_browser
    engager_browser.po.engager.load()
    agent = engager_browser.config.agent
    engager_browser.ac.engager.login(agent['login'], agent['password'])


@then('agent should receive chat session from "{customers_name}" with "{messages_count}" message')
def agent_should_receive_session(context, customers_name, messages_count):
    engager = context.browsers['engager']['first'].po.engager
    assert engager.tab_list.has_tab_with_title("(" + messages_count + ") " + customers_name) is True


@step('agent opens chat session')
def agent_opens_chat_session(context):
    engager = context.browsers['engager']['first'].po.engager
    engager.tab_list.open_incomming_message()


@then('agent should receive customers message "{message_text}"')
def agent_should_receive_message(context, message_text):
    engager = context.browsers['engager']['first'].po.engager

    assert engager.post_tab.get_last_livechat_message() == message_text

@step('agent sends message "{message_text}"')
def agent_sends_message(context, message_text):
    engager = context.browsers['engager']['first'].po.engager
    engager.tracy.close()
    engager.reply_box.send_message_form.message_input.set(message_text)
    engager.reply_box.send_message_form.submit_button.click()

@then('agent should see is typing message')
def agent_should_see_is_typing_message(context):
    engager = context.browsers['engager']['first'].po.engager
    engager.post_tab.get_is_typing_livechat_message()

@step('agent sends note "{note_text}"')
def agent_sends_note(context, note_text):
    engager = context.browsers['engager']['first'].po.engager

    engager.reply_box.note_tab.click()
    engager.reply_box.send_message_form.message_input.set(note_text)
    engager.reply_box.send_message_form.submit_button.click()

@then('agent should see note "{note_text}"')
def agent_should_receive_message(context, note_text):
    engager = context.browsers['engager']['first'].po.engager

    assert engager.post_tab.get_last_note_message() == note_text
