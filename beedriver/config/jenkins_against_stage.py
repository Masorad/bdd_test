#
# IMPORTANT! DO NOT USE IT ON YOUR LOCAL MACHINE.
#            It can interfere with Jenkins Job.
#

engager_url = 'http://engager-stage.brandembassy.com/'
reset_livechat_queue_url = 'http://cron-standard-stage.brandembassy.com/\
    cron/live-chat-agents-sessions-counter-fixer/fix'

office = {
    'url': 'http://office-stage.brandembassy.com',
    'login_name': 'hejna@brandembassy.com',
    'login_password': 'TVu6N1xz',
}

livechat_url = 'https://vps-web-utils.awsbrandembassy.com/' \
               + 'livechat-window-gherkin/'

brand_id = '1073'  # Gherkin's Selenium Brand

agent = {
    'login': "gherkin@brandembassy.com",
    'password': "ztX2ndLn",
}
