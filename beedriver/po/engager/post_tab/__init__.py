from beedriver.po.page_object import PageObject
from .locators import PostTabLocators


class PostTab(PageObject):
    def get_last_livechat_message(self):
        tab_workspace = self.find()
        message_elements = tab_workspace.find_elements_by_class_name(
            PostTabLocators.LIVE_CHAT_MESSAGE_CLASS
        )
        last_message = message_elements[-1]

        return last_message.find_element_by_class_name(
            PostTabLocators.LIVE_CHAT_MESSAGE_TEXT_CLASS
        ).text

    def get_is_typing_livechat_message(self):
        tab_workspace = self.find()
        message_elements = tab_workspace.find_elements_by_class_name(
            PostTabLocators.LIVE_CHAT_MESSAGE_CLASS)
        last_message = message_elements[-1]

        return last_message.find_element_by_class_name(
            PostTabLocators.LIVE_CHAT_IS_TYPING_CLASS
        )

    def get_last_note_message(self):
        tab_workspace = self.find()
        notes_elements = tab_workspace.find_elements_by_class_name(
            PostTabLocators.NOTE_CLASS)
        last_note = notes_elements[-1]

        note_content = last_note.find_elements_by_class_name(
            PostTabLocators.NOTE_CONTENT_CLASS
        )

        return note_content[0].text

    def get_ghost_livechat_message(self):
        tab_workspace = self.find()
        ghost_message = tab_workspace.find_elements_by_class_name(
            PostTabLocators.LIVE_CHAT_GHOST_MESSAGE_CLASS
        )

        return ghost_message.find_element_by_class_name(
            PostTabLocators.LIVE_CHAT_MESSAGE_TEXT_CLASS
        ).text
