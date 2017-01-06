class SendMessageFormLocators:
    BASE_CLASS = "//*[contains(@class,'reply-box')]"

    MESSAGE_INPUT = "//textarea"
    SUBMIT_BUTTON = "//*[contains(@class,'reply-button')]"

    NOTE_TAB_CLASS = "//*[contains(@class,'note-tab')]"
    SEND_TRANSCRIPT = "//*[contains(@class,'live-chat-transcript') and contains(@class,'action')]"
    TRANSCRIPT_SEND_SUCCESS = "//*[contains(@class,'green-box')]"
    EMAIL_INPUT = "//*[contains(@class,'input') and contains(@type, 'email')]"
    SEND_TRANSCRIPT_EMAIL_BUTTON = "//*[contains(@class,'live-chat-transcript')]/div"
