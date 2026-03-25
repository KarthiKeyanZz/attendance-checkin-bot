import pickle
import time

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import settings  


BRAVE_PATH = "/usr/bin/brave-browser"


def save_login_session():
    options = uc.ChromeOptions()
    options.binary_location = BRAVE_PATH
    options.add_argument("--start-maximized")

    driver = uc.Chrome(options=options)
    wait = WebDriverWait(driver, 20)

    driver.get("https://payroll.razorpay.com/login")

    print("\n👉 Auto-filling credentials...")

    try:
        email_input = wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='email']"))
        )
        email_input.clear()
        email_input.send_keys(settings.EMAIL)

        password_input = driver.find_element(By.XPATH, "//input[@type='password']")
        password_input.clear()
        password_input.send_keys(settings.PASSWORD)

        print("✅ Credentials filled")
        print("👉 Solve CAPTCHA and click login")

    except Exception as e:
        print("❌ Failed to auto-fill:", e)
        driver.quit()
        return

    print("⏳ Waiting for successful login...")

    try:
        wait.until(lambda driver: "dashboard" in driver.current_url)

        print("✅ Login detected!")
        print("Current URL:", driver.current_url)

    except Exception:
        print("❌ Login not detected. Try again.")
        driver.quit()
        return

    print("Current URL:", driver.current_url)

    cookies = driver.get_cookies()
    pickle.dump(cookies, open("cookies.pkl", "wb"))

    print("✅ Cookies saved successfully")

    driver.quit()


if __name__ == "__main__":
    save_login_session()