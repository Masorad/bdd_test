# BDD tests
### Installation
You need to have installed:
- **python**
- python bindings to **selenium**
- python module **behave**

Then depending on the browser of you choice:
- **Firefox**
or
- **Chrome**
- **java**
- **selenium standalone server**
- **chromedriver**

## How to run tests
### using Firefox (default)
Either
```$ behave feature_name.feature```
or
```$ BEHAVE_BROWSER=firefox behave feature_name.feature```

### using Chrome
Run selenium server and then
```$ BEHAVE_BROWSER=chrome behave feature_name.feature```

