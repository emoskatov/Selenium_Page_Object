# Test automation using Selenium

___

1) **Install virtual env all requirements**:

    ```
   python -m venv venv 
   venv\Scripts\activate.bat
   pip install -r requirements.txt
    ```

2) Download Selenium WebDriver from https://chromedriver.chromium.org/downloads (choose version which is compatible with
   your browser).<br>
   *Install to the PATH folder or to the root folder of the project*


3) **Run tests**:
   ```
   pytest -v --tb=line 
   ```
   __Option:__ the ability to select the default browser language (for example: ru, en, fr, de, es), the browser (
   Chrome or Yandex- ** only if the Yandex driver is installed**) and the test marker
    ```
   pytest -v --tb=line  -m "login_guest" --language=en --browser_name=chrome
   ```
