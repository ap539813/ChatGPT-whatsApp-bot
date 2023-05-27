from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set the path of the chromedriver.exe
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open WhatsApp
driver.get('https://web.whatsapp.com/')

# Wait for the user to scan the QR code
wait = WebDriverWait(driver, 600)
print('Scan QR Code, And then Enter')
input()
print("Logged In")

while True:
    try:
        # Wait for the specific contact to show up
        target = '"Bhaiya 😜😜🤗💛❤️ Pandey"'  # replace 'Contact Name' with the name of your WhatsApp contact or their phone number
        x_arg = '//span[contains(@title,' + target + ')]'
        group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
        group_title.click()

        # Detect new message by checking the presence of a specific HTML element
        msg_got = driver.find_elements(By.CSS_SELECTOR, "span.selectable-text.invisible-space.copyable-text")
        msg = [message.text for message in msg_got]

        if msg:
            msg_box = driver.find_elements(By.CLASS_NAME, '_21Ahp')
            msg_box.send_keys("Hi, I received the message" + Keys.ENTER)
    except Exception as e:
        print("An error occurred: ", e)
        continue
    time.sleep(10)  # Wait for 10 seconds before checking for new messages
