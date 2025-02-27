from selenium import webdriver
import time

def main():
    # Initialize the WebDriver
    driver = webdriver.Chrome()
    
    # Open the URL
    driver.get("https://app-staging.nokodr.com/")
    print("Website opened successfully!")
    
    # Wait for 5 seconds
    time.sleep(5)
    
    # Close the browser
    driver.quit()

if __name__ == "__main__":
    main()

#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def main():
    driver = webdriver.Chrome()
    driver.get("https://app-staging.nokodr.com/signup")
    
    ValidateMandatoryFields(driver)
    TestValidInputs(driver)
    TestInvalidInputs(driver)
    
    driver.quit()

def ValidateMandatoryFields(driver):
    try:
        name_field = driver.find_element(By.NAME, "name")
        email_field = driver.find_element(By.NAME, "email")
        password_field = driver.find_element(By.NAME, "password")
        confirm_password_field = driver.find_element(By.NAME, "confirmPassword")
        
        if name_field and email_field and password_field and confirm_password_field:
            print("All mandatory fields are present.")
        else:
            print("Mandatory fields are missing.")
    except:
        print("Mandatory fields are missing.")

def TestValidInputs(driver):
    driver.find_element(By.NAME, "name").send_keys("ValidName")
    driver.find_element(By.NAME, "email").send_keys("validemail@example.com")
    driver.find_element(By.NAME, "password").send_keys("ValidPass123!")
    driver.find_element(By.NAME, "confirmPassword").send_keys("ValidPass123!")
    
    driver.find_element(By.XPATH, "//button[contains(text(), 'Sign Up')]").click()
    
    time.sleep(3)
    
    try:
        success_message = driver.find_element(By.XPATH, "//*[contains(text(), 'Account created successfully!')]")
        print("Signup successful with valid inputs.")
    except:
        print("Success message not found.")

def TestInvalidInputs(driver):
    fields = ["name", "email", "password", "confirmPassword"]
    for field in fields:
        driver.find_element(By.NAME, field).clear()
    
    driver.find_element(By.NAME, "name").send_keys("InvalidName")
    driver.find_element(By.NAME, "email").send_keys("invalidemail")
    driver.find_element(By.NAME, "password").send_keys("ValidPass123!")
    driver.find_element(By.NAME, "confirmPassword").send_keys("ValidPass123!")
    
    driver.find_element(By.XPATH, "//button[contains(text(), 'Sign Up')]").click()
    time.sleep(3)
    
    try:
        error_message = driver.find_element(By.XPATH, "//*[contains(text(), 'Invalid email format')]")
        print("Error message displayed for invalid email format.")
    except:
        print("No error message for invalid email format.")
    
    driver.find_element(By.NAME, "email").clear()
    driver.find_element(By.NAME, "email").send_keys("validemail@example.com")
    driver.find_element(By.NAME, "password").clear()
    driver.find_element(By.NAME, "password").send_keys("ValidPass123!")
    driver.find_element(By.NAME, "confirmPassword").clear()
    driver.find_element(By.NAME, "confirmPassword").send_keys("DifferentPass123!")
    
    driver.find_element(By.XPATH, "//button[contains(text(), 'Sign Up')]").click()
    time.sleep(3)
    
    try:
        password_error_message = driver.find_element(By.XPATH, "//*[contains(text(), 'Passwords do not match')]")
        print("Error message displayed for passwords not matching.")
    except:
        print("No error message for mismatched passwords.")
    
    for field in fields:
        driver.find_element(By.NAME, field).clear()
    
    driver.find_element(By.XPATH, "//button[contains(text(), 'Sign Up')]").click()
    time.sleep(3)
    
    try:
        missing_fields_error_message = driver.find_element(By.XPATH, "//*[contains(text(), 'This field is required')]")
        print("Error message displayed for missing mandatory fields.")
    except:
        print("No error message for missing fields.")
    
    driver.find_element(By.NAME, "name").send_keys("NameWithSpecialChars!@#")
    driver.find_element(By.NAME, "email").send_keys("edgecaseemail@example.com")
    driver.find_element(By.NAME, "password").send_keys("ValidPass123!")
    driver.find_element(By.NAME, "confirmPassword").send_keys("ValidPass123!")
    
    driver.find_element(By.XPATH, "//button[contains(text(), 'Sign Up')]").click()
    time.sleep(3)
    
    try:
        special_chars_error_message = driver.find_element(By.XPATH, "//*[contains(text(), 'Invalid characters')]")
        print("Error message displayed for special characters in the name field.")
    except:
        print("No error message for special characters.")

if __name__ == "__main__":
    main()
