from Test_suites.BaseTest import BaseTest
from Page.BasePage import BasePage
import time
import random

class TestAddIdea(BaseTest):

    def test_add_idea(self):
        base_page = BasePage()
        base_page.get_url()
        base_page.click(base_page.button_add_idea)
        text = 'Shvabra kadabra'
        base_page.write_text(base_page.name_idea, text)
        base_page.write_text(base_page.description_ideas, text)
        base_page.write_text(base_page.expected_effect, text)
        base_page.write_text(base_page.necessary_resources, text)
        base_page.write_text(base_page.user_name, text)
        phone = '0932985505'
        base_page.write_text(base_page.phone_number, phone)
        list_select = base_page.check_is_all_elements(base_page.list_select_last_part)
        work_place = list_select[0]
        cityes = list_select[1]
        addres = list_select[2]
        base_page.click(work_place)
        base_page.click(cityes)
        list_cityes = base_page.check_is_all_elements(base_page.list_cities)
        some_cityes = random.choice(list_cityes)

        some_cityes.click()


        base_page.click(addres)


        time.sleep(5)



        # base_page.click(base_page.button_submit)
        # expected_element = base_page.check_is_element_present(base_page.pop_up_successful)
        # assert expected_element is True
        # time.sleep(3)




