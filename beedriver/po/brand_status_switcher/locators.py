elem_by_id = "//*[@id='{}']"
status_label = elem_by_id.format('status')

class BrandStatusSwitcherLocators:

    ONLINE_BUTTON = elem_by_id.format('on')
    OFFLINE_BUTTON = elem_by_id.format('off')

    def label_by_status(status):
        if not status in {'online', 'offline'}:
            status = 'online' if status else 'offline'
        return "{}[text()='{}']".format(status_label, status)

