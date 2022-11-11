# Copyright (C) by Pietrobon Andrea - All Rights Reserved
#
# This file (data.py) is part of the project: twitch-stream-viewer
# It can only be distributed from Andrea Pietrobon's official Github profile
# The use of the project twitch-stream-viewer or of this file is authorized only for personal purposes
# The redistribution, sale or commercial use of the files
# indicated without the written consent of the author is not authorized
#
# Written by Pietrobon Andrea <pietrobonandrea@yahoo.it>, Nov 2022
# Official Website <https://pietrobonandrea.com>
# Github <https://github.com/Piero24>

# Driver Path
PATH_chrome = r"YOUR-CHROME-DRIVER-PATH/chromedriver"
PATH_firefox = r"YOUR-GECKO-DRIVER-PATH/geckodriver"

# Google e-mail and Twitch e-mail
email = 'YOUR-TWITCH-MAIL'
# Twitch Username
usr = 'YOUR-TWITCH-USERNAME'
# Twitch Password
pswd = 'YOUR-TWITCH-PASSWORD'
# The Browser used for start the bot (On macOS/Linux Firefox is strongly raccomanded. Chrome isn't complete)
chousen_browser = 'Firefox' #'Chrome'

driver = ''

# Twitch developer data
twitch_ID = 'YOUR-TWITCH-DEVELOPER-ID'
twitch_KEY = 'YOUR-TWITCH-DEVELOPER-KEY'

# Streamer name and link
streamer_name = 'STREAMER-NAME'
streamer_link = 'https://www.twitch.tv/' + streamer_name

# Status of the stream (online/offline)
stream_Status = ''
# Status of the bot (1/0)
stream_already_started = 0
# Value to enable messages during the stream
mid_time_msg = 1


#List of phrases to be sent in the chat at startup
start_msg_txt_list = ['Weiiii', 'Heiii', 'Hi', 'Hi Dude!']
#List of phrases to be sent in the chat during the stream
msg_txt_list = ['Nice Game!', 'GG', '😂😂', 'Niceee', 'Top', ]