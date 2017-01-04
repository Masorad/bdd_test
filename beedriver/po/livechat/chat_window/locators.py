class ChatWindowLocators:
    STATUS_ELEMENT_OFFLINE = "//*[contains(@class,'be-chat__status--offline')]"
    STATUS_ELEMENT_ONLINE = "//*[contains(@class,'be-chat__status--online')]"
    BEGIN_CONVERSATION_BUTTON = "//*[contains(@class,'orange-button')]"

    START_CHAT_FORM = "//form"
    OFFLINE_FORM = "//*[contains(@class,'form')]"

    STATUS = "//*[contains(@class,'be-chat__status')]"

    HEADER_COLLAPSED = "//*[contains(@class,'be-chat--minimize')]"
    HEADER_EXPANDED = "//*[contains(@class,'control-panel__icon--minimize')]"

    CONVERSATION = "//*[@class='scroll-box']"
    REPLY_BOX = "//*[@class='reply-box']"

    END_CHAT_BOX = "//*[contains(@class,'be-chat__content--session-closed')]"
    SENT_SUCCESS_GREEN_BOX = "//*[contains(@class,'green-box')]"

