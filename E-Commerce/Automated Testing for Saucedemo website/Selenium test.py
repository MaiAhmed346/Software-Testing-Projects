import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# -------- Setup --------
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
wait = WebDriverWait(driver, 10)

# -------- Create screenshots folder --------
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

def take_screenshot(name):
    filename = f"screenshots/{name}_{int(time.time())}.png"
    driver.save_screenshot(filename)
    print(f"📸 Screenshot saved: {filename}")

# -------- Open Website --------
driver.get("https://www.saucedemo.com/")
take_screenshot("homepage")

# ---------- Test Case 1: Valid Login ----------
wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

wait.until(EC.url_contains("inventory"))
assert "inventory" in driver.current_url

take_screenshot("login_success")
print("✅ Test Case 1 Passed: Valid Login")

# ---------- Test Case 2: Add to Cart ----------
add_btn = wait.until(
    EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
)
add_btn.click()

cart_badge = wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
)

assert cart_badge.text == "1"
take_screenshot("add_to_cart")
print("✅ Test Case 2 Passed: Add to Cart")

# ---------- Test Case 3: Logout ----------
menu_btn = driver.find_element(By.ID, "react-burger-menu-btn")
menu_btn.click()

logout_btn = wait.until(
    EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
)
logout_btn.click()

wait.until(EC.url_contains("saucedemo"))
assert "saucedemo" in driver.current_url

take_screenshot("logout")
print("✅ Test Case 3 Passed: Logout")

# -------- Keep browser open --------
input("Press Enter to close browser...")

driver.quit()