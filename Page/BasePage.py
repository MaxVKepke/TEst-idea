from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utilities.DriverWrapper import DriverWrapper


class BasePage:

    button_add_idea = (By.CSS_SELECTOR, 'a[href*="create-idea"]')

    """Elements locators on add ideas form"""
    categories_ideas = (By.CSS_SELECTOR, 'label.form-field div.multiselect')
    name_idea = (By.CSS_SELECTOR, 'input[placeholder="Назва ідеї"]')
    description_ideas = (By.CSS_SELECTOR, 'textarea[placeholder="Опис ідеї"]')
    expected_effect = (By.CSS_SELECTOR, 'textarea[placeholder="Очікуванний ефект"]')
    necessary_resources = (By.CSS_SELECTOR, 'textarea[placeholder="Необхідні ресурси"]')
    user_name = (By.CSS_SELECTOR, 'input[placeholder*="Ваше"]')
    phone_number = (By.CSS_SELECTOR, 'input[placeholder="(0xx)-xxx-xx-xx"]')
    multiselect_work_place = (By.CSS_SELECTOR, 'div.form-field-wrapper.second div.multiselect')
    list_select_last_part = (By.CSS_SELECTOR, 'div.second span.multiselect__single')
    list_cities = (By.CSS_SELECTOR, 'div.multiselect.multiselect--active ul.multiselect__content li')

    list_address = (By.CSS_SELECTOR, 'div.current-city ul.multiselect__content li')
    button_submit = (By.CSS_SELECTOR, 'button[type="submit"]')
    pop_up_successful = (By.CSS_SELECTOR, 'div.modal-content')

    wait_element_time = 20

    def __init__(self):
        self.driver = DriverWrapper.get_webdriver()
        self.wait = WebDriverWait(self.driver, self.wait_element_time)

    def check_is_element_present(self, element_locator):
        try:
            self.wait.until(EC.presence_of_element_located(element_locator))
        except Exception:
            return False

    def check_is_all_elements(self, element_locator):
        element_list = self.wait.until(EC.presence_of_all_elements_located(element_locator))
        return element_list

    def click(self, element_locator):
        try:
            element = self.wait.until(EC.presence_of_element_located(element_locator), 'element not found')
            element.click()
        except Exception:
            element_locator.click()
        return self

    def write_text(self, element_locator, text):
        element = self.wait.until(EC.presence_of_element_located(element_locator), "method write_text can't fined element")
        element.send_keys(text)
        return self

    def get_url(self):
        """ Get url page which you are """
        url = self.driver.current_url
        print("\nCURRENT URL\n ------------------- " + url + " ----------------------")
        return url



