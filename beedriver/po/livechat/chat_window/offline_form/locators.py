def input_by_label(label):
    return "//*[preceding-sibling::*[contains(text(),'{}')]]".format(label)


class OfflineFormLocators:

    NAME = input_by_label('Name')
    EMAIL = input_by_label('Email')
    MESSAGE = input_by_label('Message')
    BUTTON = "//*[contains(@class,'button')]"

