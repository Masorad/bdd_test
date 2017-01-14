class MyViewsLocators:

    MY_VIEW_BY_NAME = "//*[contains(@class,'view') and contains(@class,'settings')]" \
                      + "/*[contains(@class,'text') and text() = '###VIEW_NAME###']//parent::*"

    def get_locator_for_view_by_name(self, view_name):
        return self.MY_VIEW_BY_NAME.replace("###VIEW_NAME###", view_name)
