from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# URL = "https://stgcrm.rnit.solutions"
# username = "admin@faceify.me"
URL = "https://faceify-corp.rnit.solutions"
username = "admin@r.com"


# URL = "https://testproduction.faceify.app"

def login(driver):
    """
    Login function for the Faceify application.

    Args:
        driver: Selenium WebDriver instance
    """
    try:
        driver.get(f"{URL}/web")

        # Enter username
        username_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter username']"))
        )
        username_field.send_keys(username)

        # Enter password
        password_field = driver.find_element(By.XPATH, "//input[@placeholder='Enter password']")
        password_field.send_keys("Rnit@123")

        # Click login button
        login_button = driver.find_element(By.XPATH, "//button[text()='Login']")
        login_button.click()

        # Wait for toast message
        toast_message = WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element((By.ID, "toast-1-description"), "Loggedin Successfully")
        )

        assert toast_message, "Login was not successful"

    except Exception as e:
        print(f"Login failed: {e}")
        raise e


def login_pages(driver):
    """
    Simplified login function for the Faceify application pages.

    Args:
        driver: Selenium WebDriver instance
    """
    try:
        # Wait for page to load
        WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter username']"))
        )

        # Enter username
        username_field = driver.find_element(By.XPATH, "//input[@placeholder='Enter username']")
        username_field.click()
        username_field.send_keys(username)

        # Enter password
        password_field = driver.find_element(By.XPATH, "//input[@placeholder='Enter password']")
        password_field.send_keys("Rnit@123")

        # Click login button
        login_button = driver.find_element(By.XPATH, "//button[text()='Login']")
        login_button.click()

        # Note: The original code commented out the toast verification,
        # so I'm also leaving it out here

    except Exception as e:
        print(f"Login failed: {e}")
        raise e