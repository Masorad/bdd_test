from selenium import webdriver

base_class = webdriver.Remote
config = {
    'command_executor': 'http://seleniumhub:4444/wd/hub',
    'desired_capabilities': {
        'browserName': 'firefox',
        'javascriptEnabled': True
    }
}
