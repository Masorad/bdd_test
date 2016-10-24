import time

from behave import step


@step('"{somebody}" waits for "{sleep_value}" seconds')
def wait_for_x_seconds(context, somebody, sleep_value):
    time.sleep(int(sleep_value))
