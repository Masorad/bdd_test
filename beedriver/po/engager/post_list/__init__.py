from beedriver.po.elements.button import Button
from beedriver.po.elements.checkbox import CheckBox
from beedriver.po.engager.post_list.locators import PostListLocators
from beedriver.po.page_object import PageObject


class PostList(PageObject):
    def init_child_objects(self):
        check_all_box_selector = '//*[@id="' + PostListLocators.CHECK_ALL_BOX_ID + '"]'
        self.check_all_box = CheckBox(self, check_all_box_selector, dont_chain_xpath=True)
        self.set_as_resolved_button = Button(self, PostListLocators.SET_AS_RESOLVED_BUTTON)

    def get_number_of_posts(self):
        tab_workspace = self.find()
        posts = tab_workspace.find_elements_by_class_name(PostListLocators.ITEMS_IN_POST_LIST_CLASS)

        return len(posts)
