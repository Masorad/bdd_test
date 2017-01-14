from beedriver.po.page_object import PageObject
from beedriver.po.engager.left_panel.my_views.my_view import MyView
from beedriver.po.engager.left_panel.my_views.locators import MyViewsLocators


class MyViews(PageObject):

    def get_my_view_by_name(self, view_name):
        my_views_locators = MyViewsLocators()
        return MyView(self, my_views_locators.get_locator_for_view_by_name(view_name))
