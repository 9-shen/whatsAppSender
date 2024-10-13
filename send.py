import pywhatkit as kit
import pandas as pd
import time
import logging
import os
import random

import config

# Configure logging to track sent messages
logging.basicConfig(filename='message_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

# Read the CSV file containing names and phone numbers, making sure numbers are strings
contacts = pd.read_csv(config.Contacts + '/contacts.csv', dtype={'number': str})

# Path to the Messages folder
messages_folder = config.Messages + '/'

# Get a list of all text files in the Messages folder
message_files = [file for file in os.listdir(messages_folder) if file.endswith('.txt')]

# Counter for sent messages
sent_count = 0

# Define the minimum and maximum delay in seconds (to randomize delay)
min_delay = 10  # minimum delay
max_delay = 120  # maximum delay

# Send messages
for index, contact in contacts.iterrows():
    name = contact['name']
    number = contact['number']

    # Randomly select a message file
    selected_message_file = random.choice(message_files)

    # Read the message from the randomly selected file
    with open(os.path.join(messages_folder, selected_message_file), 'r', encoding='utf-8') as file:
        message_template = file.read()

    # Format the message with the contact's name if needed
    message = message_template.format(name=name)

    # Check if the number starts with a '+' sign, if not, add it
    if not number.startswith('+'):
        number = f'+{number}'

    try:
        # Send a WhatsApp message and close the tab after sending
        kit.sendwhatmsg_instantly(number, message, wait_time=20, tab_close=True, close_time=5)

        # Increment the counter
        sent_count += 1

        # Log the successful message
        logging.info(f"Message sent to {name} ({number}) using {selected_message_file}")

        # Randomize the delay between messages
        delay_between_messages = random.randint(min_delay, max_delay)
        time.sleep(delay_between_messages)

    except Exception as e:
        logging.error(f"Failed to send message to {name} ({number}) using {selected_message_file}. Error: {e}")

print(f"Messages sent successfully! Total messages sent: {sent_count}")

# Log the final count of sent messages
logging.info(f"Total messages sent: {sent_count}")
