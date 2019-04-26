import pytest
from utilities.DriverWrapper import DriverWrapper
import requests

@pytest.mark.usefixtures('get_browser_name')
@pytest.mark.usefixtures('get_base_host')
@pytest.mark.usefixtures('get_base_url')
class BaseTest:

    def setup(self):
        self.driver = DriverWrapper.get_webdriver()
        try:
            self.driver.maximize_window()
            self.driver.get(self.base_url)

        except Exception as error:
            DriverWrapper.close_driver()
            pytest.fail('setup test failed: {}'.format(error))

    def teardown(self):
        DriverWrapper.close_driver()

