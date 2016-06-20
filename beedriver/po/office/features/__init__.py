from beedriver.po.page_object import PageObject
from .locators import FeaturesLocators

class Features(PageObject):

    def load(self):
        config = self.client.config
        base_office_url = config.office['url']
        brand_id = config.brand_id
        url = '{}/brands/detail/features-list/id/{}/'.format(
            base_office_url, brand_id)
        self.client.get(url)

    def is_enabled(self, feature):
        locator = FeaturesLocators.feature_status_by_url(feature)
        state_element = self.client.find_element_by_xpath(locator)
        state = state_element.get_attribute('class')
        return state == FeaturesLocators.ENABLED_CLASS

    def ensure_feature_is_in_state(self, feature, desired_state):
        if desired_state == self.is_enabled(feature):
            return

        locator = FeaturesLocators.feature_toggle_by_url(feature)
        toggle_element = self.client.find_element_by_xpath(locator)
        toggle_element.click()

