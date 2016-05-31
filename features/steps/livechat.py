from behave import given, when, then, step
from helpers import validate_step_input
    

@step('customer opens brand page')
def customer_opens_brand_page(context):
    livechat_browser = context.BeeDriver(**context.browser_config)
    context.browsers['livechat']['first'] = livechat_browser
    livechat_browser.po.livechat.load()


@step('customer {resize_action} chat window')
def step_impl(context, resize_action):
    valid_resize_actions = {'expands', 'collapses'}
    validate_step_input(resize_action, valid_resize_actions)

    chat_window = context.browsers['livechat']['first'].po.livechat.chat_window
    if resize_action == 'expands':
        chat_window.expand()
    elif resize_action == 'collapses':
        chat_window.collapse()


@then('chat window should be {size}')
def step_impl(context, size):
    valid_sizes = {'collapsed', 'expanded'}
    validate_step_input(size, valid_sizes)

    chat_window = context.browsers['livechat']['first'].po.livechat.chat_window
    if size == 'collapsed':
        assert chat_window.is_collapsed() is True
    elif size == 'expanded':
        assert chat_window.is_expanded() is True


@then('chat window status should be {status}')
def step_impl(context, status):
    valid_statuses = {'offline', 'online'}
    validate_step_input(status, valid_statuses)

    chat_window = context.browsers['livechat']['first'].po.livechat.chat_window
    if status == 'online':
        assert chat_window.is_online() is True
    else:
        assert chat_window.is_online() is False


@then('chat window should show static form for starting new chat')
def step_impl(context):
    start_chat_form = context.browsers['livechat']['first'].po.livechat.chat_window.start_chat_form
    start_chat_form.wait_for_exist()
    start_chat_form.name.wait_for_exist()
    start_chat_form.submit_button.wait_for_exist()

