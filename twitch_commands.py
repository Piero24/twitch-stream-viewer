# Copyright (C) by Pietrobon Andrea - All Rights Reserved
#
# This file (twitch_commands.py) is part of the project: twitch-stream-viewer
# It can only be distributed from Andrea Pietrobon's official Github profile
# The use of the project twitch-stream-viewer or of this file is authorized only for personal purposes
# The redistribution, sale or commercial use of the files
# indicated without the written consent of the author is not authorized
#
# Written by Pietrobon Andrea <pietrobonandrea@yahoo.it>, Nov 2022
# Official Website <https://pietrobonandrea.com>
# Github <https://github.com/Piero24>

# Imported modules
import time
import data
import requests
import random
from selenium import webdriver
from selenium.webdriver.common.by import By



def start_twitch_viewer(streamer_link) -> list:
    """Opens the browser via the selenium drivers 
        (you can choose between chrome and firefox) 
        at the link provided. After that if is necessary
        it will try to login with your twitch occount.

    Args:
        streamer_link: Link of the twitch channel to connect to.

    Returns:
        A list containing three values.
        driver: It keeps and data concerning the process (used to close or carry out future operations).
        start: Contains an empty string if everything went well on startup.
        login: Contains an empty string if everything went well in the account login phase.

    """

    start = ''
    login = ''

    try:

        if data.chousen_browser == 'Firefox':
            
            brw_options = webdriver.FirefoxOptions()
            brw_options.add_argument("-profile")
            brw_options.add_argument(data.firefox_arg)
            driver = webdriver.Firefox(executable_path=data.PATH_firefox, options=brw_options)

        elif data.chousen_browser == 'Chrome':

            brw_options = webdriver.ChromeOptions()
            brw_options.add_argument(data.chrome_arg)
            brw_options.add_argument("profile-directory=Profile 3")
            brw_options.add_experimental_option("detach", True)
            driver = webdriver.Chrome(executable_path=data.PATH_chrome, options=brw_options)
        
        driver.set_window_position(0, 0)
        driver.set_window_size(1440, 900)
        driver.get(streamer_link)
        
    except:
        start = 'Problem on starting the selected driver'
    

    try:
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, "div[class='Layout-sc-nxg1ff-0 csWXEI']").click()
        time.sleep(5)
        username=driver.find_element(By.CSS_SELECTOR, "input[id='login-username']")
        time.sleep(5)
        password=driver.find_element(By.CSS_SELECTOR, "input[id='password-input']")
        time.sleep(5)
        username.clear()
        password.clear()
        time.sleep(5)
        username.send_keys(data.usr)
        time.sleep(5)
        password.send_keys(data.pswd)
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, "div[class='Layout-sc-nxg1ff-0 OZCSg']").click()

    except:
        login = 'The viewer should not prompt for a login. \n Viewer started successfully'
        
    return [driver, start, login]



def send_the_verification_code(ver_code) -> int:
    """It takes the authentication code received via 
        email to complete the login phase.

        TODO: 

    Args:
        ver_code:

    Returns:
        Return the verification code in int format received via email.

    """
    pass



def send_chat_message(driver, list_of_keywords) -> None:
    """Send a phrase from those provided in the list to the stream chat.

    Args:
        driver: It keeps and data concerning the process 
            (used to close or carry out future operations).
        list_of_keywords: List of possible keywords to send.

    """

    time.sleep(5)

    try:
        text_box = driver.find_element(By.CSS_SELECTOR, 'div[class="Layout-sc-nxg1ff-0 font-scale--default"]').click()
        time.sleep(2)
        text_box = driver.find_element(By.CSS_SELECTOR, 'button[class="ScCoreButton-sc-1qn4ixc-0 ScCoreButtonPrimary-sc-1qn4ixc-1 hisLxy dDxrgX"]').click()
    except:
        print('Error: Can\'t click the box')


    try:
        driver.find_element(By.CSS_SELECTOR, 'div[class="Layout-sc-nxg1ff-0 font-scale--default"]').click()
        text_box = driver.find_element(By.CSS_SELECTOR, 'div[data-test-selector="chat-input"]')
        time.sleep(2)
        write_on_the_input(text_box, list_of_keywords)

    except:
        print('Error: Can\'t send a message on the chat')
    

    try:
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, 'button[data-a-target="chat-send-button"]').click()
    except:
        print('Error: Can\'t click the send button')

    




def write_on_the_input(text_box, list_of_keywords) -> None:
    """Chooses the sentence to send and writes it in the textbox.

    Args:
        text_box: Where to send the message.
        list_of_keywords: List of possible keywords to send.

    """

    selected_txt = random.choice(list_of_keywords)

    for char_txt in selected_txt:
        time.sleep(random.choice(range(1, 3)))
        text_box.send_keys(char_txt)




def check_Stream_Status() -> str:
    """Check if the streamer is online or offline.

    Returns:
        Return the string online if the 
        streamer is online and offline if it is offline.

    """

    body = {
        'client_id': data.twitch_ID,
        'client_secret': data.twitch_KEY,
        "grant_type": 'client_credentials'
    }
    r = requests.post('https://id.twitch.tv/oauth2/token', body)

    keys = r.json()

    headers = {
        'Client-ID': data.twitch_ID,
        'Authorization': 'Bearer ' + keys['access_token']
    }

    stream = requests.get('https://api.twitch.tv/helix/streams?user_login=' + data.streamer_name, headers=headers)
    stream_data = stream.json()

    if len(stream_data['data']) == 1:
        stream_Status = 'online'
    else:
        stream_Status = 'offline'

    return stream_Status