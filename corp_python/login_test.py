import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from Functions import login_pages, URL


class LoginTests(unittest.TestCase):

    def setUp(self):
        """Set up the test environment before each test."""
        chrome_options = Options()
        # Uncomment below lines if you want to run tests in headless mode
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        """Clean up after each test."""
        if self.driver:
            self.driver.quit()

    def test_faceify_hrms_login(self):
        """Test login to Faceify HRMS."""
        driver = self.driver
        driver.get(f"{URL}/web")
        login_pages(driver)

        # # Verify HRMS element is present
        # WebDriverWait(driver, 10).until(
        #     EC.visibility_of_element_located((By.XPATH, "//div[text()='HRMS']"))
        # )
        # self.assertTrue(driver.find_element(By.XPATH, "//div[text()='HRMS']").is_displayed())

    def test_faceify_crm_login(self):
        """Test login to Faceify CRM."""
        driver = self.driver
        driver.get(f"{URL}/fcrm")
        login_pages(driver)

        # Note: You might want to add verification for CRM-specific elements

    # def test_faceify_fitness_login(self):
    #     """Test login to Faceify Fitness."""
    #     driver = self.driver
    #     driver.get(f"{URL}/wfitness")
    #     login_pages(driver)

        # Note: You might want to add verification for Fitness-specific elements


if __name__ == "__main__":
    unittest.main()