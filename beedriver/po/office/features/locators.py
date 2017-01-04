class FeaturesLocators:
    @classmethod
    def feature_by_url(cls, feature):
        return "//tr[descendant::*[contains(@href,'/feature/{}/')]]" \
            .format(feature)

    @classmethod
    def feature_status_by_url(cls, feature):
        feature_row = FeaturesLocators.feature_by_url(feature)
        return "{}/td[2]/span".format(feature_row)

    @classmethod
    def feature_toggle_by_url(cls, feature):
        feature_row = FeaturesLocators.feature_by_url(feature)
        return "{}/td[3]/a".format(feature_row)

    ENABLED_CLASS = 'green'
