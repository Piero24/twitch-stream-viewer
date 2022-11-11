# Copyright (C) by Pietrobon Andrea - All Rights Reserved
#
# This file (main.py) is part of the project: twitch-stream-viewer
# It can only be distributed from Andrea Pietrobon's official Github profile
# The use of the project twitch-stream-viewer or of this file is authorized only for personal purposes
# The redistribution, sale or commercial use of the files
# indicated without the written consent of the author is not authorized
#
# Written by Pietrobon Andrea <pietrobonandrea@yahoo.it>, Nov 2022
# Official Website <https://pietrobonandrea.com>
# Github <https://github.com/Piero24>

# Imported modules
import data
import time
import twitch_commands as t_cmd

def main():

    time.sleep(900)
    data.stream_Status = t_cmd.check_Stream_Status()
    #print(data.stream_Status)

    # If the streamer is online and if the bot hasn't started yet
    if data.stream_Status == 'online' and data.stream_already_started == 0:

        data.driver = t_cmd.start_twitch_viewer(data.streamer_link)[0]
        data.stream_already_started = 1
        t_cmd.send_chat_message(data.driver, data.start_msg_txt_list)
    
    # If the streamer is offline and if the bot is still active
    elif data.stream_Status == 'offline' and data.stream_already_started == 1:
        data.driver.quit()
        data.stream_already_started = 0
    
    # If the streamer is online and if the bot is already active 
    # and you want messages during the stream
    elif data.stream_Status == 'online' and data.stream_already_started == 1 and data.mid_time_msg == 1:
        t_cmd.send_chat_message(data.driver, data.msg_txt_list)


if __name__ == "__main__":
    while 1: main()

