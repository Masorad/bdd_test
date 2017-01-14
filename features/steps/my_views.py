from behave import then, when
from helpers import validate_step_input
import time


@then('agent should see "{number_of_posts}" items in list of posts')
def agent_should_see_number_of_items_in_list_of_posts(context, number_of_posts):

    tab_list = context.browsers['engager']['first'].po.engager.post_tab

    assert tab_list.get_number_of_posts() == int(number_of_posts)


@then('agent should see view with name "{view_name}"')
def agent_should_see_view_with_name(context, view_name):

    my_views = context.browsers['engager']['first'].po.engager.left_panel.my_views
    my_view = my_views.get_my_view_by_name(view_name)

    assert my_view.exists()


@then('view with name "{view_name}" is "{view_state}"')
def view_with_name_is_in_given_state(context, view_name, view_state):

    valid_states = {'active', 'not active'}
    validate_step_input(view_state, valid_states)

    my_views = context.browsers['engager']['first'].po.engager.left_panel.my_views
    my_view = my_views.get_my_view_by_name(view_name)

    if view_state == 'active':
        assert my_view.is_active() is True
    else:
        assert my_view.is_active() is False


@when(u'agent clicks on view "{view_name}"')
def agent_clicks_on_view(context, view_name):

    my_views = context.browsers['engager']['first'].po.engager.left_panel.my_views
    my_view = my_views.get_my_view_by_name(view_name)
    my_view.click()
    time.sleep(2)
