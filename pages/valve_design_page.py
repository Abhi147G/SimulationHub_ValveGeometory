from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image, ImageChops



class ValveDesignPageSelenium:
    BASE_URL = "https://experiments.simulationhub.com/valve-design"

    # Locators
    DROPDOWN_BTN_XPATH = "/html/body/div[3]/div/div/div[1]/div[2]/div/div/div[2]/div[1]/div[2]/button/span[1]"
    SECOND_OPTION_XPATH = "/html/body/div[3]/div/div/div[1]/div[2]/div/div/div[2]/div[1]/div[2]/div/ul/li[2]"
    PREDICT_BTN_XPATH = "//button[contains(text(),'Predict') or contains(text(),'Evaluate')]"
    VALVE_DIAMETER_SLIDER_XPATH = "//html/body/div[3]/div/div/div[1]/div[2]/div/div/div[2]/div[2]/div[2]/span/span[6]" 

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def goto(self, url: str = None):
        """Navigate to Valve Design page"""
        self.driver.get(url or self.BASE_URL)

    def open_dropdown(self):
        """Click the Valve Type dropdown"""
        dropdown = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.DROPDOWN_BTN_XPATH)))
        dropdown.click()

    def select_second_valve_type(self) -> str:
        """Click the 2nd option and return its text"""
        option = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.SECOND_OPTION_XPATH)))
        option_text = option.get_attribute("textContent").strip()
        option.click()
        return option_text

    def is_predict_btn_visible(self) -> bool:
        """Check if Predict button is visible"""
        try:
            btn = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.PREDICT_BTN_XPATH)))
            return btn.is_displayed()
        except:
            return False

    def set_valve_diameter_slider(self, value: int):
        """Set the Valve Diameter (DN) using the slider"""
        slider = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.VALVE_DIAMETER_SLIDER_XPATH)))
        actions = ActionChains(self.driver)
        # Move slider: click and drag by offset 
        actions.click_and_hold(slider).move_by_offset(value, 0).release().perform()


    def take_screenshot(self, file_path):
        """Take a screenshot of the current page."""
        self.driver.save_screenshot(file_path)

