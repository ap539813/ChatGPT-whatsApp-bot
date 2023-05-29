from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime, timedelta

import json
import openai

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

with open('secrets.json') as f:
    data = json.load(f)

openai.api_key = data['api_key']

messages = [
    {"role": "system", "content": "Personal assistsnt for queries, I am a software developer, python developer, data science and machine learning developer, I also take classes on these topics"},
]

del data

def clean_text(msg):
    return msg.replace('\n', '').replace('\ue008\ue007\ue008', '').replace('`', '').replace('(Keys.SHIFT)+(Keys.ENTER)+(Keys.SHIFT)', '')

def chat_response(input_message):
    global messages
    if input_message:
        messages.append({
            'role': 'user', 'content': input_message
        })
        chat = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo", messages = messages
        )

    reply = chat.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    return reply

last_message_text = ''
my_last_message = ''

if __name__ == "__main__":
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

            # Convert the timestamp to a datetime object
            timestamp = datetime.strptime(timestamp_str, "%I:%M %p")

            # Update the year, month and day of the timestamp to match the current date
            timestamp = timestamp.replace(year=current_date.year, month=current_date.month, day=current_date.day)

            # Get the current time
            current_time = datetime.now()

            
            # print((current_time - timestamp), repr(last_message_text), repr(my_last_message), repr(message_text))
            # If the message was sent less than 60 seconds ago, respond to it
            if (current_time - timestamp < timedelta(seconds=70)) and (clean_text(last_message_text)[:200] != clean_text(message_text)[:200]) and (clean_text(my_last_message)[:200] != clean_text(message_text)[:200]):
                print("messaging")
                my_message = chat_response(message_text).replace('\n', (Keys.SHIFT)+(Keys.ENTER)+(Keys.SHIFT))
                # my_message = 'Hi this is the message I want to send \n but this shouldnt go in the next line'.replace('\n', (Keys.SHIFT)+(Keys.ENTER)+(Keys.SHIFT))
                msg_box = driver.find_elements(By.CLASS_NAME, '_3Uu1_')[0]
                msg_box.send_keys(my_message + Keys.ENTER)
                last_message_text = clean_text(message_text)
                my_last_message = clean_text(my_message)
        except Exception as e:
            print("An error occurred: ", e)
            continue
        time.sleep(10)  # Wait for 10 seconds before checking for new messages