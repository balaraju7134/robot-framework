from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.by import By

class TextField:
    """Custom keywords for <lib-textfield>"""

    def __init__(self):
        self.selib = BuiltIn().get_library_instance('SeleniumLibrary')

    def enter_textfield_by_label(self, label, text, index=1):
        """Enter text using label"""
        driver = self.selib.driver
        xpath = f"(//lib-textfield[.//label[contains(text(), '{label}')]])[{index}]//input"

        self.selib.wait_until_element_is_visible(f"xpath={xpath}", timeout=10)

        element = driver.find_element(By.XPATH, xpath)
        element.clear()
        element.send_keys(text)

        self.selib.log(f"Entered '{text}' in textfield with label='{label}' index={index}", level='INFO')

    def enter_textfield_by_placeholder(self, placeholder, text, index=1):
        """Enter text using placeholder"""
        driver = self.selib.driver
        xpath = f"(//lib-textfield[.//input[@placeholder='{placeholder}']])[{index}]//input"

        self.selib.wait_until_element_is_visible(f"xpath={xpath}", timeout=10)

        element = driver.find_element(By.XPATH, xpath)
        element.clear()
        element.send_keys(text)

        self.selib.log(f"Entered '{text}' in textfield with placeholder='{placeholder}' index={index}", level='INFO')

    def enter_textfield_by_label_and_placeholder(self, label, placeholder, text, index=1):
        """Enter text using both label and placeholder"""
        driver = self.selib.driver
        xpath = f"(//lib-textfield[.//label[contains(text(), '{label}')] and .//input[@placeholder='{placeholder}']])[{index}]//input"

        self.selib.wait_until_element_is_visible(f"xpath={xpath}", timeout=10)

        element = driver.find_element(By.XPATH, xpath)
        element.clear()
        element.send_keys(text)

        self.selib.log(
            f"Entered '{text}' in textfield with label='{label}', placeholder='{placeholder}', index={index}",
            level='INFO'
        )