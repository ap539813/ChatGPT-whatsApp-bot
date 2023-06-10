# ChatGPT-whatsApp-bot

This is a Python script that uses the Selenium library to create a chatbot for WhatsApp. The chatbot reads incoming messages and generates responses using the OpenAI GPT-3.5 Turbo model.

## Prerequisites

Before running the script, make sure you have the following installed:

- Python (version 3.6 or later)
- Selenium library (`pip install selenium`)
- OpenAI Python library (`pip install openai`)
- Chrome WebDriver

Please note that this script has been tested with Chrome WebDriver. You may need to download the appropriate version of the WebDriver based on your Chrome browser version. You can download the Chrome WebDriver from the following link: [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

## Setup

1. Clone or download the repository to your local machine.
2. Install the required libraries by running the following command:
```shell
pip install -r requirements.txt
```
3. Create a file named `secrets.json` in the same directory as the script. This file will contain your OpenAI API key. The `secrets.json` file should have the following structure:
```json
{
    "api_key": "YOUR_OPENAI_API_KEY"
}
```

Replace "YOUR_OPENAI_API_KEY" with your actual OpenAI API key

## Usage

1. Open a terminal or command prompt and navigate to the directory where the script is located.
2. Run the script using the following command:
```shell
python chatbot.py
```
3. The script will open a Chrome browser window and navigate to the WhatsApp web page (https://web.whatsapp.com/).
4. Use your phone to scan the QR code displayed on the browser window to log in to WhatsApp.
5. Once logged in, the script will wait for incoming messages.
6. When a new message is received, the chatbot will generate a response using the OpenAI GPT-3.5 Turbo model.
7. The chatbot will send the generated response back to the sender on WhatsApp.

## Customization

You can customize the behavior of the chatbot by modifying the following parts of the script:

* target: Change the value of the target variable to the name or phone number of the contact or group you want the chatbot to respond to.
* messages: Modify the messages list to add initial messages that will be sent to the OpenAI GPT-3.5 Turbo model before generating a response. You can provide system-level instructions or any other context you want the model to consider.
* my_message: Customize the content of the message that the chatbot sends as a response. Modify the my_message variable to change the response message.

## Notes
* The script will check for new messages every 10 seconds. You can adjust this interval by modifying the value of time.sleep(10) in the script.
* The script compares the timestamp of the last message to the current time to determine if a response should be generated. You can modify the time window by changing the value of timedelta(seconds=70) to a different duration.
* The script removes certain characters from the messages to clean them before sending to the OpenAI GPT-3.5 Turbo model. You can modify the clean_text() function if you want to customize the cleaning process.

## Disclaimer
This script is provided as-is without any warranty. Use it at your own risk. Be aware of the terms of service and usage policies of WhatsApp and OpenAI when using this script.
