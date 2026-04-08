from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.by import By

class TextArea:
    """Custom keywords for <lib-textarea>"""

    def __init__(self):
        self.selib = BuiltIn().get_library_instance('SeleniumLibrary')

    def enter_textarea_by_label(self, label, text, index=1):
        """Enter text in textarea using label (index starts from 1)"""
        if index < 1:
            raise ValueError("Index should start from 1")

        driver = self.selib.driver

        xpath = f"(//lib-textarea[.//label[contains(text(), '{label}')]])[{index}]//textarea"

        self.selib.wait_until_element_is_visible(f"xpath={xpath}", timeout=10)

        element = driver.find_element(By.XPATH, xpath)
        element.clear()
        element.send_keys(text)

        self.selib.log(
            f"Entered '{text}' in textarea with label='{label}' index={index}",
            level='INFO'
        )

    def enter_textarea_by_placeholder(self, placeholder, text, index=1):
        """Enter text in textarea using placeholder (index starts from 1)"""
        if index < 1:
            raise ValueError("Index should start from 1")

        driver = self.selib.driver

        xpath = f"(//lib-textarea[.//textarea[@placeholder='{placeholder}']])[{index}]//textarea"

        self.selib.wait_until_element_is_visible(f"xpath={xpath}", timeout=10)

        element = driver.find_element(By.XPATH, xpath)
        element.clear()
        element.send_keys(text)

        self.selib.log(
            f"Entered '{text}' in textarea with placeholder='{placeholder}' index={index}",
            level='INFO'
        )

    def enter_textarea_by_label_and_placeholder(self, label, placeholder, text, index=1):
        """Enter text using both label and placeholder"""
        if index < 1:
            raise ValueError("Index should start from 1")

        driver = self.selib.driver

        xpath = f"(//lib-textarea[.//label[contains(text(), '{label}')] and .//textarea[@placeholder='{placeholder}']])[{index}]//textarea"

        self.selib.wait_until_element_is_visible(f"xpath={xpath}", timeout=10)

        element = driver.find_element(By.XPATH, xpath)
        element.clear()
        element.send_keys(text)

        self.selib.log(
            f"Entered '{text}' in textarea with label='{label}', placeholder='{placeholder}', index={index}",
            level='INFO'
        )