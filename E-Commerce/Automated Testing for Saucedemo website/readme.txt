# 🧪 SauceDemo Automation Testing Project

## 📌 Project Overview

This project demonstrates end-to-end automated testing for the SauceDemo web application using Selenium WebDriver with Python.

The automation simulates real user behavior, covering key functional scenarios such as login, adding items to the cart, and logout. The project also includes validation checks and screenshots as execution evidence.

---

## 🎯 Objectives

* Validate core user flows of the application
* Ensure system behavior matches expected results
* Demonstrate automation testing skills using real scenarios
* Provide test execution evidence (screenshots)

---

## 🧪 Test Scenarios

### 1. Valid Login

* **Description:** Verify that a user can log in with valid credentials
* **Steps:**

  1. Navigate to login page
  2. Enter valid username and password
  3. Click login button
* **Expected Result:** User is redirected to inventory page

---

### 2. Add Product to Cart

* **Description:** Verify that a user can add a product to the cart
* **Steps:**

  1. Login with valid credentials
  2. Click "Add to Cart" for a product
* **Expected Result:** Cart badge displays "1"

---

### 3. Logout

* **Description:** Verify that a user can log out successfully
* **Steps:**

  1. Open menu
  2. Click logout
* **Expected Result:** User is redirected to login page

---

## ⚙️ Automation Details

* **Language:** Python
* **Framework:** Selenium WebDriver
* **Test Type:** End-to-End Functional Testing
* **Wait Strategy:** Explicit Wait (WebDriverWait)
* **Assertions:** Used to validate expected results
* **Screenshots:** Captured during execution for validation

---

## 📷 Test Evidence

Screenshots are captured automatically during test execution and stored in the `screenshots/` folder.

Examples:

* Login Success
* Add to Cart
* Logout

---

---

## 💡 Key Highlights

* Simulates real user workflow
* Uses explicit waits instead of static delays
* Includes assertions for validation
* Captures screenshots for reporting and debugging
* Clean and simple structure suitable for demonstration

---

## 🚀 Future Improvements

* Convert tests to Pytest framework
* Implement Page Object Model (POM)
* Add negative test cases (invalid login)
* Integrate API testing
* Add test reporting (HTML reports)

---

## 👩‍💻 Author

Mai Kamal Abdelatif Ahmed
Automation & QA Enthusiast
