# Tesco Booker v1.0
# Download chromedriver for script to function

from selenium import webdriver
import time
import sys
import os
from datetime import datetime
from datetime import timedelta

# Load driver
if os.name == 'nt':
  import winsound
  driver = webdriver.Chrome('./driver/chromedriver.exe')
else:
  driver = webdriver.Chrome('./driver/chromedriver')

driver.set_window_position(0, 0)
driver.set_window_size(800, 900)

# Load url
driver.get("https://secure.tesco.com/account/en-GB/login")
current_url = driver.current_url

# Wait for user to login and add items to basket
while current_url != "https://www.tesco.com/groceries/en-GB/slots/delivery":
    current_url = driver.current_url
    time.sleep(2)

# Loop forever
out = 0
while True:

  # Iterate over days for three weeks
  for i in range(21):
    date = (datetime.now() + timedelta(days=i) ).strftime('%Y-%m-%d')
    url = "https://www.tesco.com/groceries/en-GB/slots/delivery/" + date + "?slotGroup=1"
    driver.get(url);

    print ("Checking " + str(date))

    # Check for slot message and break if didnt find element
    try:
      slot_message = driver.find_element_by_class_name('slot-list--none-available')
    except:
      out = 1
      break

    # Sleep
    time.sleep(1.5)

  # Break out main loop
  if out == 1:
    break

# Cause sound for detection of a available slot
for i in range(15):
  if os.name == 'nt':
    frequency = 2500
    duration = 1000
    winsound.Beep(frequency, duration)
  else:
    sys.stdout.write('\a')
    sys.stdout.flush()
