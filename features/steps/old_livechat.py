import time
from behave import given, when, then, step
from helpers import validate_step_input

@step('customer opens brand page with old chat')
def customer_opens_brand_page_with_old_chat(context):
    old_livechat_browser = context.BeeDriver()
    context.browsers['old_livechat']['first'] = old_livechat_browser
    old_livechat_browser.po.old_livechat.load()

@then('old chat window status should be "{status}"')
def old_chat_window_status_should_be_status(context, status):
    valid_statuses = {'offline', 'online'}
    validate_step_input(status, valid_statuses)

    chat_window = context.browsers['old_livechat']['first'].po.old_livechat.chat_window

    # When the chat loads, it is offline by default for a brief moment.
    time.sleep(1)

    if status == 'online':
        assert chat_window.is_online() is True
    else:
        assert chat_window.is_online() is False

