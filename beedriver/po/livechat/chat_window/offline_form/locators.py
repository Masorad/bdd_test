def input_by_label(label):
    return "/*[@name='{}']".format(label)
    # return "//*[preceding-sibling::*[contains(text(),'{}')]]".format(label)


class OfflineFormLocators:
    NAME = input_by_label('name')
    EMAIL = input_by_label('email')
    MESSAGE = input_by_label('message')
    BUTTON = "/following-sibling::button[@class='orange-button']"
