import time

from behave import when, then, step
from helpers import validate_step_input

from beedriver.po.livechat import LiveChatLocators


@step('customer opens brand page')
def step_impl(context):
    context.execute_steps('Then "first" customer opens brand page')


@step('"{identifier}" customer opens brand page')
def customer_opens_brand_page(context, identifier):
    livechat_browser = context.BeeDriver()
    livechat_browser.po.livechat.load()
    iframe_id = livechat_browser.find_element_by_class_name(LiveChatLocators.CHAT_WINDOW_IFRAME_CLASS_NAME)
    livechat_browser.switch_to_frame(iframe_id)
    context.browsers['livechat'][identifier] = livechat_browser


@step('customer "{resize_action}" chat window')
def step_impl(context, resize_action):
    context.execute_steps('Then "first" customer "' + resize_action + '" chat window')


@step('"{identifier}" customer "{resize_action}" chat window')
def step_impl(context, identifier, resize_action):
    valid_resize_actions = {'expands', 'collapses'}
    validate_step_input(resize_action, valid_resize_actions)

    chat_window = context.browsers['livechat'][identifier].po.livechat.chat_window
    if resize_action == 'expands':
        chat_window.expand()
    elif resize_action == 'collapses':
        chat_window.collapse()


@step('customer fills "{customers_name}" into name input')
def step_impl(context, customers_name):
    context.execute_steps('Then "first" customer fills "' + customers_name + '" into name input')


@step('"{identifier}" customer fills "{customers_name}" into name input')
def step_impl(context, identifier, customers_name):
    form = context.browsers['livechat'][identifier].po.livechat.chat_window.start_chat_form
    form.wait_for_exist()
    form.name.set(customers_name)
    form.submit_button.click()


@when('customer submits online form in chat window')
def step_impl(context):
    context.execute_steps('Then "first" customer submits online form in chat window')


@step('"{identifier}" customer submits online form in chat window')
def customer_submits_online_form_in_chat_window(context, identifier):
    form = context.browsers['livechat'][identifier].po.livechat.chat_window.start_chat_form
    form.wait_for_exist()
    form.submit_button.click()
    time.sleep(1)


@then('chat window should be "{size}"')
def step_impl(context, size):
    valid_sizes = {'collapsed', 'expanded'}
    validate_step_input(size, valid_sizes)

    chat_window = context.browsers['livechat']['first'].po.livechat.chat_window
    if size == 'collapsed':
        assert chat_window.is_collapsed() is True
    elif size == 'expanded':
        assert chat_window.is_expanded() is True


@then('chat window status should be "{status}"')
def step_impl(context, status):
    valid_statuses = {'offline', 'online'}
    validate_step_input(status, valid_statuses)

    chat_window = context.browsers['livechat']['first'].po.livechat.chat_window
    if status == 'online':
        assert chat_window.is_online() is True
    else:
        assert chat_window.is_online() is False


@then('chat window should show "{status}" form')
def step_impl(context, status):
    valid_statuses = {'offline', 'online'}
    validate_step_input(status, valid_statuses)

    chat_window = context.browsers['livechat']['first'].po.livechat.chat_window
    if status == 'online':
        form = chat_window.start_chat_form
        form.wait_for_exist()
        form.name.wait_for_exist()
        form.submit_button.wait_for_exist()
    elif status == 'offline':
        form = chat_window.offline_form
        form.wait_for_exist()
        form.name.wait_for_exist()
        form.email.wait_for_exist()
        form.message.wait_for_exist()
        form.submit_button.wait_for_exist()


@then('chat window should show conversation interface')
def step_impl(context):
    context.execute_steps('Then "first" chat window should show conversation interface')


@then('"{identifier}" chat window should show conversation interface')
def step_impl(context, identifier):
    chat_window = context.browsers['livechat'][identifier].po.livechat.chat_window
    chat_window.agent_profile.wait_for_exist()
    chat_window.conversation.wait_for_exist()
    chat_window.send_message_form.wait_for_exist()


@step('customer sends message "{message_text}"')
def step_impl(context, message_text):
    chat_window = context.browsers['livechat']['first'].po.livechat.chat_window
    chat_window.send_message_form.message_input.set(message_text)
    chat_window.send_message_form.submit_button.click()


@then('customer should receive agents message "{message_text}"')
def customer_should_recieve_message(context, message_text):
    chat_window = context.browsers['livechat']['first'].po.livechat.chat_window

    assert chat_window.conversation.get_last_message() == message_text


@step('customer types message "{message_text}"')
def step_impl(context, message_text):
    chat_window = context.browsers['livechat']['first'].po.livechat.chat_window
    chat_window.send_message_form.message_input.set(message_text)


@step('customer refreshes livechat browser')
def agent_refreshes_livechat_browser(context):
    livechat_browser = context.browsers['livechat']['first']
    livechat_browser.refresh()
    iframe_id = livechat_browser.find_element_by_class_name(LiveChatLocators.CHAT_WINDOW_IFRAME_CLASS_NAME)
    livechat_browser.switch_to_frame(iframe_id)
    time.sleep(3)


@step('customer opens chat menu')
def customer_opens_chat_menu(context):
    context.execute_steps('Then "first" customer opens chat menu')


@step('"{identifier}" customer opens chat menu')
def customer_opens_chat_menu(context, identifier):
    header = context.browsers['livechat'][identifier].po.livechat.chat_window.header
    header.toggle_chat_menu()
    header.wait_for_exist()


@step('customer clicks on close session item')
def click_on_close_session_item(context):
    context.execute_steps('Then "first" customer clicks on close session item')


@step('"{identifier}" customer clicks on close session item')
def click_on_close_session_item(context, identifier):
    item = context.browsers['livechat'][identifier].po.livechat.chat_window.header.chat_menu.close_chat_menu_item
    item.click()
    time.sleep(1)


@then('customer sees that chat session is "Closed"')
def customer_sees_that_chat_session_is_closed(context):
    chat_window = context.browsers['livechat']['first'].po.livechat.chat_window
    chat_window.end_chat_message.wait_for_exist()


@then('customer sees successufly sended transcript message')
def customer_successufly_sended_transcript_message(context):
    chat_window = context.browsers['livechat']['first'].po.livechat.chat_window
    chat_window.transcript_sent_success.wait_for_exist()


@when('customer opens transcript form')
def step_impl(context):
    chat_window = context.browsers['livechat']['first'].po.livechat.chat_window
    chat_window.settings_expander.click()
    time.sleep(1)
    chat_window.send_transcript_icon.click()


@when('customer fills e-mail "{email}"')
def step_impl(context, email):
    chat_window = context.browsers['livechat']['first'].po.livechat.chat_window
    chat_window.send_transcript_email_input.set(email)


@when('customer clicks on send button')
def step_impl(context):
    chat_window = context.browsers['livechat']['first'].po.livechat.chat_window
    chat_window.send_transcript_email_send_button.click()


@then('customer closes the transcript form')
def step_impl(context):
    chat_window = context.browsers['livechat']['first'].po.livechat.chat_window
    chat_window.send_transcript_close_button.click()


@then('customer clicks on end chat button')
def step_impl(context):
    chat_window = context.browsers['livechat']['first'].po.livechat.chat_window
    chat_window.settings_expander.click()
    time.sleep(1)
    chat_window.end_chat.click()


@then('customer clicks on send transcript link')
def step_impl(context):
    chat_window = context.browsers['livechat']['first'].po.livechat.chat_window
    chat_window.send_transcript_link.wait_for_exist()
    chat_window.send_transcript_link.click()


@then('"{identifier}" chat window should be "{number}" in queue')
def step_impl(context, identifier, number):
    chat_window = context.browsers['livechat'][identifier].po.livechat.chat_window
    chat_window.info_panel.wait_for_exist()
    assert chat_window.info_panel.get_info_text() == "Waiting for agent. You're " + number + " in queue."


@step('"{identifier}" customer ends chat session')
def step_impl(context, identifier):
    context.execute_steps('Then "' + identifier + '" customer opens chat menu')
    context.execute_steps('Then "' + identifier + '" customer clicks on close session item')
