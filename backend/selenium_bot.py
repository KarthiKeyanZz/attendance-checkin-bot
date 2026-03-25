import pickle
import os
from datetime import datetime

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import settings


BRAVE_PATH = "/usr/bin/brave-browser"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
COOKIE_PATH = os.path.join(BASE_DIR, "cookies.pkl")


def get_driver():
    options = uc.ChromeOptions()
    options.binary_location = BRAVE_PATH

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    return uc.Chrome(options=options, use_subprocess=True)


def load_cookies(driver):
    try:
        cookies = pickle.load(open(COOKIE_PATH, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)
        return True
    except Exception as e:
        print("❌ Cookie load failed:", e)
        return False


def get_attendance_url():
    now = datetime.now()
    return f"https://payroll.razorpay.com/attendance-v2?month={now.year}-{now.month:02d}"


def run_attendance(action=None):  

    try:
        driver.get("https://payroll.razorpay.com")

        if not load_cookies(driver):
            return {"status": "error", "message": "Cookies not found"}

        url = get_attendance_url()
        print("👉 Opening:", url)

        driver.get(url)

        wait = WebDriverWait(driver, 25)

        wait.until(lambda d: "attendance-v2" in d.current_url)

        print("✅ Attendance page loaded")

        buttons = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//button"))
        )

        target_button = None
        detected_action = None

        for btn in buttons:
            text = btn.text.strip()

            if action == "checkin" and "Check In" in text:
                target_button = btn
                detected_action = "checkin"
                break

            elif action == "checkout" and "Check Out" in text:
                target_button = btn
                detected_action = "checkout"
                break

            elif action is None:
                if "Check In" in text:
                    target_button = btn
                    detected_action = "checkin"
                    break
                elif "Check Out" in text:
                    target_button = btn
                    detected_action = "checkout"
                    break

        if not target_button:
            return {
                "status": "error",
                "message": "No Check In / Check Out button found"
            }

        print(f"👉 Detected action: {detected_action}")

        wait.until(EC.element_to_be_clickable(target_button))
        target_button.click()

        print(f"✅ {detected_action} clicked")

        screenshot_path = os.path.join(BASE_DIR, f"{detected_action}_success.png")
        driver.save_screenshot(screenshot_path)

        return {
            "status": "success",
            "action": detected_action,
            "message": f"{detected_action} successful",
            "screenshot": screenshot_path
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

    finally:
        driver.quit()