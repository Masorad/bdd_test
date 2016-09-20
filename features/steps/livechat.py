from behave import when, then, step
from helpers import validate_step_input

from beedriver.po.livechat import LiveChatLocators


@step('customer opens brand page')
def customer_opens_brand_page(context):
    livechat_browser = context.BeeDriver()
    livechat_browser.po.livechat.load()
    iframe_id = livechat_browser.find_element_by_class_name(LiveChatLocators.CHAT_WINDOW_IFRAME_CLASS_NAME)
    livechat_browser.switch_to_frame(iframe_id)
    context.browsers['livechat']['first'] = livechat_browser


@step('customer "{resize_action}" chat window')
def step_impl(context, resize_action):
    valid_resize_actions = {'expands', 'collapses'}
    validate_step_input(resize_action, valid_resize_actions)

    chat_window = context.browsers['livechat']['first'].po.livechat.chat_window
    if resize_action == 'expands':
        chat_window.expand()
    elif resize_action == 'collapses':
        chat_window.collapse()


@step('customer fills in valid name in chat window online form')
def step_impl(context):
    form = context.browsers['livechat']['first'].po.livechat.chat_window.start_chat_form
    form.wait_for_exist()
    form.name.set('valid name placeholder')
    form.submit_button.click()


@when('customer submits online form in chat window')
def customer_submits_online_form_in_chat_window(context):
    form = context.browsers['livechat']['first'].po.livechat.chat_window.start_chat_form
    form.wait_for_exist()
    form.submit_button.click()
    import time
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
    chat_window = context.browsers['livechat']['first'].po.livechat.chat_window
    chat_window.agent_profile.wait_for_exist()
    chat_window.conversation.wait_for_exist()
    chat_window.reply_box.wait_for_exist()
