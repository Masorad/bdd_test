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
    SETTINGS_EXPANDER = "//*[contains(@class,'icon--setting')]"
    END_CHAT = "//*[contains(@id, 'endchat')]"
    SEND_TRANSCRIPT_ICON = "//*[contains(@class, 'dropdown-menu')]/li[2]"
    SEND_TRANSCRIPT_LINK = "//*[contains(@class, 'be-chat__content--session-closed')]/p/a"
    SEND_TRANSCRIPT_EMAIL_INPUT = "//input[contains(@type, 'email')]"
    SEND_TRANSCRIPT_EMAIL_SEND_BUTTON = "//button[contains(@type, 'submit')]"
    SEND_TRANSCRIPT_CLOSE_BUTTON = "//a[contains(@class, 'close-icon')]"
    TRANSCRIPT_SENT_SUCCESS = "//*[contains(@class, 'green-box')]"
