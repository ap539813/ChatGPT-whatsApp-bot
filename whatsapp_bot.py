from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime, timedelta

# Set the path of the chromedriver.exe
driver = webdriver.Chrome()

# Open WhatsApp
driver.get('https://web.whatsapp.com/')

# Wait for the user to scan the QR code
wait = WebDriverWait(driver, 600)
print('Scan QR Code, And then Enter')
input()
print("Logged In")

# Get the current date
current_date = datetime.now().date()
target = '"Bhaiya 😜😜🤗💛❤️ Pandey"' 
x_arg = '//span[contains(@title,' + target + ')]'

last_message_text = ''
my_last_message = ''

while True:
    try:
        # Wait for the specific contact to show up
        group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
        group_title.click()

        # Detect new message by checking the last message in the conversation
        all_messages = driver.find_elements(By.CSS_SELECTOR, "div._1BOF7._2AOIt")
        last_message = all_messages[-1]
        
        # Get the timestamp from the message
        timestamp_element = last_message.find_element(By.CSS_SELECTOR, "span.l7jjieqr.fewfhwl7")
        timestamp_str = timestamp_element.text  # "12:42 am"

        # Get the message text
        message_text_element = last_message.find_element(By.CSS_SELECTOR, "span._11JPr.selectable-text.copyable-text")
        message_text = message_text_element.text
        print(message_text)

        # Convert the timestamp to a datetime object
        timestamp = datetime.strptime(timestamp_str, "%I:%M %p")

        # Update the year, month and day of the timestamp to match the current date
        timestamp = timestamp.replace(year=current_date.year, month=current_date.month, day=current_date.day)

        # Get the current time
        current_time = datetime.now()

        
        print(current_time - timestamp)
        # If the message was sent less than 60 seconds ago, respond to it
        if (current_time - timestamp < timedelta(seconds=60)) and (last_message_text != message_text) and (my_last_message != message_text):
            print(current_time - timestamp)
            print("messaging")
            my_message = "Hi, I received the message"
            msg_box = driver.find_elements(By.CLASS_NAME, '_3Uu1_')[0]
            msg_box.send_keys(my_message + Keys.ENTER)
            last_message_text = message_text
            my_last_message = my_message
    except Exception as e:
        print("An error occurred: ", e)
        continue
    time.sleep(10)  # Wait for 10 seconds before checking for new messages