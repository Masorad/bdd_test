# BDD tests
### Installation
You need to have installed:
- **python3** - instalation instructions on [official python website](http://www.python.org)
- python modules **selenium** and **behave**, both can be installed with pip:
```pip install selenium behave```

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
```$ behave feature_name.feature```, e.g. ```behave features/livechat_basic_window.feature```

### Specifying config file
If you want to specify config file, use `BEEDRIVER_BROWSER` environment variable along with the behave command, e.g.
```BEEDRIVER_BROWSER=firefox behave feature_name.feature```

### using Chrome
Run selenium server, e.g.:
```java -jar /home/$USER/bin/selenium-server-standalone-2.48.2.jar -Dwebdriver.chrome.driver=/home/$USER/bin/chromedriver```
 and then
```$ BEEDRIVER_BROWSER=chrome behave feature_name.feature```

