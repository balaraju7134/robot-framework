from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Dropdown:
    """Custom keywords for <lib-dropdown>"""

    def __init__(self):
        self.selib = BuiltIn().get_library_instance('SeleniumLibrary')

    def select_dropdown_by_label(self, label, value, index=1):
        """Select dropdown option using label (visible text)"""
        driver = self.selib.driver

        xpath = f"(//lib-dropdown[.//label[contains(text(), '{label}')]])[{index+1}]//select"

        self.selib.wait_until_element_is_visible(f"xpath={xpath}", timeout=10)

        element = driver.find_element(By.XPATH, xpath)
        select = Select(element)
        select.select_by_visible_text(value)

        self.selib.log(
            f"Selected '{value}' in dropdown with label='{label}' index={index}",
            level='INFO'
        )

    def select_dropdown_by_value(self, label, value, index=1):
        """Select dropdown option using value attribute"""
        driver = self.selib.driver

        xpath = f"(//lib-dropdown[.//label[contains(text(), '{label}')]])[{index+1}]//select"

        self.selib.wait_until_element_is_visible(f"xpath={xpath}", timeout=10)

        element = driver.find_element(By.XPATH, xpath)
        select = Select(element)
        select.select_by_value(value)

        self.selib.log(
            f"Selected value='{value}' in dropdown with label='{label}' index={index}",
            level='INFO'
        )

    def select_dropdown_by_index(self, label, option_index, index=1):
        """Select dropdown option using option index"""
        driver = self.selib.driver

        xpath = f"(//lib-dropdown[.//label[contains(text(), '{label}')]])[{index+1}]//select"

        self.selib.wait_until_element_is_visible(f"xpath={xpath}", timeout=10)

        element = driver.find_element(By.XPATH, xpath)
        select = Select(element)
        select.select_by_index(option_index)

        self.selib.log(
            f"Selected option index='{option_index}' in dropdown with label='{label}' index={index}",
            level='INFO'
        )