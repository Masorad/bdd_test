# BDD tests
These are system tests written in [python](http://www.python.org) using [Behave](http://pythonhosted.org/behave/) implementation of [Gherkin language](http://pythonhosted.org/behave/philosophy.html#the-gherkin-language).
The browser is driven by [Selenium](http://www.seleniumhq.org). Selenium can use either webdriver built in Firefox, or connect to remote selenium server (which can of course be run locally as well).

### Installation
- install **python3** - instalation instructions on [official python website](http://www.python.org)
- clone this repo ```$ git clone git@github.com:BrandEmbassy/bdd_tests.git```
- ```$ cd bdd_tests```
- create virtual environment ```$ pyvenv venv```
- activate the virtual environment ```$ source venv/bin/activate```
- install required python modules```$ pip install -r requirements.txt```

Then depending on the browser of you choice:
- **Firefox**

or
- **Chrome**
- **java** (installation is operating-system-specific)
- download **selenium standalone server** from [seleniumhq downloads page](http://www.seleniumhq.org/download/)
- download **chromedriver** from the same download page

## How to run tests
### Using Firefox
The easiest way is to use Firefox (default browser) with default config (found at beedriver/config/default.py - you need to adjust the config file, but since it is versioned, it is recommended to create custom config, see below)
```$ python -m behave feature_name.feature```, e.g. ```$ python -m behave features/livechat_basic_window.feature```

### Specifying config file
If you want to specify config file, use `BEEDRIVER_CONFIG` environment variable along with the behave command, e.g.
```$ BEEDRIVER_CONFIG=custom_123 python -m behave feature_name.feature```
(config files prefixed with `custom_` are in .gitignore)

### using Chrome
Run selenium server, e.g.:
```$ java -jar -Dwebdriver.chrome.driver="/home/$USER/bin/chromedriver" /home/$USER/bin/selenium-server-standalone.jar```
 and then
```$ BEEDRIVER_BROWSER=chrome python -m behave feature_name.feature```

## Structure of page objects
```BeeDriver``` is a subclassed selenium webdriver, with `page object` (po) tree and `action chanins` (ac) tree built upon instantiation as attributes. These are containers for underlying po/ac, etc.

## Interactive session
Apart from running tests, you can also use page objects and action chains interactively or in scripts outside of behave:
```
$ cd bdd_tests
$ python
>>> from beedriver import get_beedriver
>>> browser = get_beedriver()
>>> browser.ac.engager.login('login name', 'password')
>>> browser.po.engager.left_panel.livechat_button.is_online()
```

## Directory structure
- `beedriver` - contains BeeDriver, page objects and action chains, can be used independently of tests
- `beedriver/browser` - contains browser configs
- `beedriver/config` - contains general config (names, passwords, etc.)
- `features` - contains tests in Gherkin
- `features/steps` - contains step implementation

# Docker
```bash

# build images from docer-compose
sudo docker-compose build --no-cache

# buid herkin image with tests
sudo docker build . --tag bddtests_gherkin

# run services for delenium hub and browser
sudo docker-compose up # optional -d to run it as deamon

# run tests
sudo docker run -it --rm --sig-proxy=true --pid=host --link seleniumhub --net bddtests_default -v'/home/achse/www/brandembassy/bdd_tests:/var/app' -w'/var/app' bddtests_gherkin 
```

## Againts stage evironment

You need to have `config/custom_config.py` with this contnt:

```py
engager_url = 'http://engager-stage.brandembassy.com/'

office = {
    'url': 'http://office-stage.brandembassy.com/',
    'login_name': 'hejna@brandembassy.com',
    'login_password': 'TVu6N1xz',
}

livechat_url = 'https://vps-web-utils.awsbrandembassy.com/livechat-window-gherkin/'

brand_id = '1073'  # Gherkin's Selenium Brand

# abstract brand from this once chat window communicates with engager
brand_status_switcher_url = 'http://localhost:3000/?testing1234'

agent = {
    'login': "gherkin@brandembassy.com",
    'password': "ztX2ndLn",
}
```
