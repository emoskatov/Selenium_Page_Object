# Test automation using Selenium
___

1) **Install all requirements**:

    ```
   pip install -r requirements.txt
    ```

2) Download Selenium WebDriver from https://chromedriver.chromium.org/downloads (choose version which is compatible with your browser).
*Install to the PATH folder or to the root folder of the project*


3) **Run tests**:
   ```
   pytest -v --tb=line 
   ```
   __Optional:__ The ability to choose a default language of browser(ru or en) and browser(Chrome or Yandex- **only if yandexdriver is installed**)
    ```
   pytest -v --tb=line  -m "login_guest" --language=en --browser_name=chrome
   ```
