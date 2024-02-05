from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def automation_selenium():
    # Selenium setup
    driver = webdriver.Chrome()  # Make sure to have the appropriate WebDriver installed for your browser and in the PATH

    # Navigate to the form page
    driver.get("https://example.com/form")

    # Fill out the form
    name_field = driver.find_element("name", "name")
    name_field.send_keys("Your Name")

    email_field = driver.find_element("name", "email")
    email_field.send_keys("your@email.com")

    message_field = driver.find_element("name", "message")
    message_field.send_keys("Example message")

    # Submit the form
    message_field.send_keys(Keys.RETURN)

    # Close the browser
    driver.quit()

if __name__ == "__main__":
    automation_selenium()
