# BDD tests
These are system tests written in [python](http://www.python.org) using [Behave](http://pythonhosted.org/behave/) implementation of [Gherkin language](http://pythonhosted.org/behave/philosophy.html#the-gherkin-language).
The browser is driven by [Selenium](http://www.seleniumhq.org). Selenium can use either webdriver built in Firefox, or connect to remote selenium server (which can of course be run locally as well).

### Installation
- install **python3** - instalation instructions on [official python website](http://www.python.org)
- clone this repo ```$ git clone git@github.com:BrandEmbassy/bdd_tests.git```
- ```$ cd bdd_tests```
- create virtual environment ```$ pyvenv venv```
- activate the virtual environment ```$ source venv/bin/activate```
- install required python modules```$ pip install -r requrements.txt```

Then depending on the browser of you choice:
- **Firefox**

or
- **Chrome**
- **java** (installation is operating-system-specific)
- download **selenium standalone server** from [seleniumhq downloads page](http://www.seleniumhq.org/download/)
- download **chromedriver** from the same download page

## How to run tests
### Using Firefox
The easiest way is to use Firefox (default browser) with default config (found at beedriver/config/default.py)
```$ python -m behave feature_name.feature```, e.g. ```$ python -m behave features/livechat_basic_window.feature```

### Specifying config file
If you want to specify config file, use `BEEDRIVER_CONFIG` environment variable along with the behave command, e.g.
```$ BEEDRIVER_CONFIG=default python -m behave feature_name.feature```

### using Chrome
Run selenium server, e.g.:
```$ java -jar /home/$USER/bin/selenium-server-standalone-2.48.2.jar -Dwebdriver.chrome.driver=/home/$USER/bin/chromedriver```
 and then
```$ BEEDRIVER_BROWSER=chrome python -m behave feature_name.feature```

