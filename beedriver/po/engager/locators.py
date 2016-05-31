app_body = "body[@id='be-app']"
main_search = "descendant::input[@class='main-search']"

class EngagerLocators:

    LOGIN_PAGE = "//body[@id='login']"
    LEFT_PANEL = "//*[contains(@class,'left-panel ')]"
    CARE = "//{}[not({})]".format(app_body, main_search)
    CRM = "//{}[{}]".format(app_body, main_search)

