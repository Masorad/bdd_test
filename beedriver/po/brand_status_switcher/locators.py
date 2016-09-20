elem_by_id = "//*[@id='{}']"


class BrandStatusSwitcherLocators:
    ONLINE_BUTTON = elem_by_id.format('on')
    OFFLINE_BUTTON = elem_by_id.format('off')
