from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.by import By
import time

class DatePicker:
    """Custom keywords for <lib-datepicker>"""

    def __init__(self):
        self.selib = BuiltIn().get_library_instance('SeleniumLibrary')

    def select_date_by_label(self, label, year, month, day, index=1):
        """
        Select date from datepicker using label (index starts from 1)
        Example: year=2026, month=March, day=15
        """
        if index < 1:
            raise ValueError("Index should start from 1")

        driver = self.selib.driver

        base_xpath = f"(//lib-datepicker[.//label[normalize-space()='{label}']])[{index}]"
        input_xpath = base_xpath + "//input"

        # Scroll & open datepicker
        self.selib.scroll_element_into_view(f"xpath={input_xpath}")
        self.selib.wait_until_element_is_visible(f"xpath={input_xpath}", timeout=10)
        driver.find_element(By.XPATH, input_xpath).click()

        # Popup base (same logic as your RF code)
        dp_popup = base_xpath + "/following::div[contains(@class,'custom-close')][1]"

        # Open year selection
        year_btn = f"({dp_popup}//span)[2]"
        self.selib.wait_until_element_is_visible(f"xpath={year_btn}", timeout=10)
        driver.find_element(By.XPATH, year_btn).click()

        # Navigate to correct year range
        for _ in range(50):
            years_text = driver.find_element(By.XPATH, f"({dp_popup}//div)[1]/div").text
            start_year = int(years_text.split("-")[0].strip())
            end_year = int(years_text.split("-")[1].strip())

            if year >= start_year and year <= end_year:
                break
            elif year < start_year:
                self._click_back_year(dp_popup)
            else:
                self._click_forward_year(dp_popup)

            time.sleep(0.5)

        # Select year
        year_xpath = f"({dp_popup}//div)[2]/div[normalize-space()='{year}']"
        self.selib.wait_until_element_is_visible(f"xpath={year_xpath}", timeout=10)
        driver.find_element(By.XPATH, year_xpath).click()

        # Open month selection
        month_btn = f"({dp_popup}//span)[1]"
        self.selib.wait_until_element_is_visible(f"xpath={month_btn}", timeout=10)
        driver.find_element(By.XPATH, month_btn).click()

        # Select month
        month_xpath = f"{dp_popup}//div[normalize-space()='{month}']"
        self.selib.wait_until_element_is_visible(f"xpath={month_xpath}", timeout=10)
        driver.find_element(By.XPATH, month_xpath).click()

        # Select day
        day_xpath = f"({dp_popup}//button/time)[normalize-space()='{day}']"
        self.selib.wait_until_element_is_visible(f"xpath={day_xpath}", timeout=10)
        driver.find_element(By.XPATH, day_xpath).click()

        self.selib.log(
            f"Selected date {day}-{month}-{year} for label='{label}' index={index}",
            level='INFO'
        )

    def get_date_by_label(self, label, index=1):
        """Get value from datepicker input"""
        if index < 1:
            raise ValueError("Index should start from 1")

        driver = self.selib.driver

        xpath = f"(//lib-datepicker[.//label[normalize-space()='{label}']])[{index}]//input"

        self.selib.wait_until_element_is_visible(f"xpath={xpath}", timeout=10)

        value = driver.find_element(By.XPATH, xpath).get_attribute("value")

        self.selib.log(
            f"Fetched date '{value}' from label='{label}' index={index}",
            level='INFO'
        )

        return value

    # ---------------- Helper Methods ---------------- #

    def _click_back_year(self, dp_popup):
        xpath = f"{dp_popup}//i[contains(@class,'fa-angle-left')]"
        self.selib.wait_until_element_is_visible(f"xpath={xpath}", timeout=10)
        self.selib.driver.find_element(By.XPATH, xpath).click()

    def _click_forward_year(self, dp_popup):
        xpath = f"{dp_popup}//i[contains(@class,'fa-angle-right')]"
        self.selib.wait_until_element_is_visible(f"xpath={xpath}", timeout=10)
        self.selib.driver.find_element(By.XPATH, xpath).click()