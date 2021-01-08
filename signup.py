#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert 
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import schedule
import time

# These are the paths to the actual chromium driver and to the adblocker respectively
PATH = "/Applications/chromedriver"
path_to_adblocker = "/Users/musamalik/Desktop/Projects/Gym/1.30.6_0"

# Activates chrome options which lets you cutsomize your chromium instance
chrome_options = webdriver.ChromeOptions()
# Causes all chrome notifications to be disabled automatically so that notifcation popups do not occur
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
# Adds an argument to chrome options to load the uBlock Origin extension
chrome_options.add_argument('load-extension=' + path_to_adblocker)

# Sets driver to load chrome from the chromium driver specified while customizing it using the chrome options I specified above
driver = webdriver.Chrome(options=chrome_options, executable_path= PATH)

driver.get("https://www.imleagues.com/spa/fitness/5e8104afb444441885eb6b0fd41c48d4/home")

# Goes to login page
try:
    login = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "LOGIN"))
    ).click()

except:
    print("login page error")
    driver.quit()
    exit()

# Types in email and clicks return
try:
    email = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "email"))
    )
    email.send_keys("YOUR EMAIL")
    email.send_keys(Keys.RETURN)

except:
    print("email error")
    driver.quit()
    exit()

# Types in password and clicks return
try:
    password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    password.send_keys("YOUR PASSWORD")
    password.send_keys(Keys.RETURN)

except:
    print("password error")
    driver.quit()
    exit()

# Goes to the page with all the classes
try:
    fitness = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Fitness/Swim"))
    )
    fitness.click()

except:
    print("fitness/swim error")
    driver.quit
    exit()

# Selects the day time frame for all sessions
try:
    day = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "day"))
    )

    # Scrolls down to make sure "day" is shown on screen because an ad might be covering it and causes the program to crash
    driver.execute_script("window.scrollTo(0, 600)")

    day.click()

except:
    print("day error")
    driver.quit()
    exit()

# Selects the next arrow to select the next day since the sign up occurs a day in advance
try:
    next_arrow = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "►"))
    )
    next_arrow.click()
    
except:
    print("arrow error")
    driver.quit()
    exit()

# Opens the dropdown to select only 1202 sessions and then closes the dropdown 
try:
    dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "multiselect-selected-text"))
    )
    dropdown.click()

    room_selection = driver.find_element_by_class_name("multiselect-container")
    room_selection.find_element_by_partial_link_text("1202 - ").click()

    dropdown.click()

except:
    print("dropdown error")
    driver.quit()
    exit()

# Store all the times into a list and then iterate through the list to find the desired times
try:
    time.sleep(3)

    list_container = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "fc-list-event-container"))
    )
    times = [] 
    times = list_container.find_elements_by_class_name("fc-list-event-time")
    for items in times:
        if items.text == "11:30am" or items.text == "1:45pm":
            items.click()
            break

except:
    print("list error")
    driver.quit()
    exit()

# Click sign up the first time
try:
    sign_up = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Sign Up"))
    )

     # Scrolls down to make sure "Sign Up" is shown on screen because an ad might be covering it and causes the program to crash
    driver.execute_script("window.scrollTo(0, 1500)")

    sign_up.click()

except:
    print("first signup error")
    exit()

# Click sign up the second time
try:
    sign_up = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary"))
    )

    # Scrolls down to make sure "Sign Up" is shown on screen because an ad might be covering it and causes the program to crash
    driver.execute_script("window.scrollTo(0, 900)")

    sign_up.click()

except:
    print("second signup error")
    exit()
