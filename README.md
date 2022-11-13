<div id="top"></div>

<!-- BADGE -->
[![](https://img.shields.io/github/release-date/piero24/Template-README)]()
[![](https://img.shields.io/github/last-commit/piero24/Template-README)]()
[![Maintenance](https://img.shields.io/badge/Maintained-yes-green.svg)](https://github.com/Piero24/Template-README)
<!--[![Maintenance](https://img.shields.io/badge/Maintained%3F-no-red.svg)](https://github.com/Piero24/Template-README) -->
[![](https://img.shields.io/github/issues/piero24/Template-README)]()
[![](https://img.shields.io/github/issues-pr/piero24/Template-README)]()
[![](https://img.shields.io/github/downloads/piero24/Template-README/total)]()

[![](https://img.shields.io/github/license/piero24/Template-README)]()
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](code_of_conduct.md)


<!--
*** You can make other badges here
*** [shields.io](https://shields.io/)
*** or here
*** [CircleCI](https://circleci.com/)
-->
<br/>

<!-- Working ✅ Work in progress ⚠️ ~~Deprecate~~ ⛔️ -->
**Project Status:** Work in progress ⚠️ <a href="#maintenance">⇩</a>
<br/>
**Percentage Completely:** 70% 🔋 <a href="#roadmap">⇩</a>
<br/>
<br/>

<p align="center">
  <img src="https://www.freepnglogos.com/uploads/twitch-tv-user-logos-4.png" width="200" height="150">
</p>

<h1 align="center">
    <a href="https://github.com/Piero24/twitch-stream-viewer">Twitch-Stream-Viewer</a>
</h1>

<p align="center">
    Script to automatically start the browser when your favorite streamer is online
    <br/>
    <a href="#documentation"><strong>Explore the docs »</strong></a>
    <br/>
    <br/>
    <a href="https://github.com/Piero24/twitch-stream-viewer/issues">Report Bug</a>
    •
    <a href="https://github.com/Piero24/twitch-stream-viewer/issues">Request Feature</a>
  </p>


---



<h2 id="itroduction" align="center"><br/><br/><br/>📔  Itroduction  📔</h2>
          
<p align="center">
  This short python script allows you to automatically start the browser (for the moment it is only available with firefox) to see your favorite streamer. In case you are a streamer you can use it to verify that everything is going correctly in your stream.
  <br/>
  <br/>
  <br/>
  <img src="https://vanschneider.com/blog/content/images/wp-content/uploads/2019/09/02a_Ultimate_Logo.gif">
  <br/>
  <br/>
</p>



<h2 id="prerequisites" align="center"><br/>🧰  Prerequisites  🧰</h2>

<p align="center">
  <br/>
  There are some prerequisites needed to be able to use this script.
  <p align="center">
  1) Have <a href="https://www.mozilla.org/en-US/firefox/new/">Firefox</a> installed as a browser
  </p>
  <p align="center">
  2) You have logged in with your browser account (if you don't have one you have to create it)
  </p>
  <p align="center">
  3) Be registered on the <a href="https://dev.twitch.tv">Twitch developer</a> portal (have your twitch ID and your twitch KEY)
  </p>
  <p align="center">
  4) Downloaded the <a href="https://github.com/mozilla/geckodriver/releases">Selenium drivers</a> for Firefox
  </p>
</p>
  
<p align="right"><a href="#top">⇧</a></p>



<h2 id="how-to-start" align="center"><br/>⚙️  How to Start  ⚙️</h2>

<p align="center"> 
  1. Install what you need to make everything work

  ```sh
  pip install requests
  pip install selenium
  ```
</p>
<br/>
<p align="center">
  2. Rename <b>data_empty.py</b> to <b>data.py</b>
</p>
<br/>
<p align="center">
  3. Login to twitch with you credential (The code should work even without this step but it is highly recommended to do so as it may not work if twitch requests the verification code by mail at login)
</p>
<br/>
<p align="center">
  4. In the data.py file, enter the path to the folder where the account profile used to log in to firefox is.
  <br/><br/>
  In my case (on mac) it looks like this:

  ```python
  firefox_arg = "/Users/username/Library/Application Support/Firefox/Profiles/axglk2qpm.default-release"
  ```
  <p align="center">Now enter the path of the selenium driver</p>

  ```python
  PATH_firefox = r"/Users/username/Documents/twitch-stream-viewer/geckodriver"
  ```

</p>
<p align="center">
  5. Complete the following fields with the required data
  
  ```python
  # Google e-mail and Twitch e-mail
  email = 'YOUR-TWITCH-MAIL'
  # Twitch Username
  usr = 'YOUR-TWITCH-USERNAME'
  # Twitch Password
  pswd = 'YOUR-TWITCH-PASSWORD'

  # Twitch developer data
  twitch_ID = 'YOUR-TWITCH-DEVELOPER-ID'
  twitch_KEY = 'YOUR-TWITCH-DEVELOPER-KEY'

  # Streamer name and link
  streamer_name = 'STREAMER-NAME'
  ```
</p>
<br/><br/>
<p align="center">
  Now everything is ready. To start it in the terminal, go to the folder containing the script and write
  
  ```ssh
  python3 main.py
  ```
</p>

<br/><br/>
<p align="center">
  <b>Tips:</b>
  The bot sends messages as soon as it connects to greet the stream and at regular intervals during the stream to show that it is still there. If you want to change the phrases just change them in the data.py file.
  
  If you want to remove the messages during the stream and have only those at the beginning, just set the following in the data.py file.
  
  ```python
  mid_time_msg = 0
  ```
</p>

<p align="right"><a href="#top">⇧</a></p>


---
 
 <h2 id="license" align="center"><br/><br/><br/>🔍  License  🔍</h2>

<p align="center">
  The licensing section is divided into:
  <br/>
  <br/>
  - <a href="#general-license">General License</a>
  <br/>
  - <a href="#authors-and-copyright">Authors and Copyright</a>
  <br/>
  <br/>
  The 
  <a href="#general-license">General License</a> 
   indicates the base license chosen for the code.
  <br/>
  While 
  <a href="#authors-and-copyright">Authors and Copyright</a> 
   indicates who are the authors and who owns the copyright of the code.
  <br/>
</p>

<br/>


<h3 id="general-license" align="center"><br/>🖋  General License  🖋</h3>

<p align="center">
  <strong>GNU GENERAL PUBLIC LICENSE</strong>
  <br/>
  <i>Version 3, 29 June 2007</i>
  <br/>
  <br/>
  <i>Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/></i>
  <br/>
  <i>Everyone is permitted to copy and distribute verbatim copies</i>
  <br/>
  <i>of this license document, but changing it is not allowed.</i>
  <br/>
  <br/>
  <i>Preamble</i>
  <br/>
  <i>The GNU General Public License is a free, copyleft license for</i>
  <br/>
  <i>software and other kinds of works.</i>
  <br/>
  <br/>
  <a href="https://github.com/Piero24/Template-README/blob/main/LICENSE"><strong>License Documentation »</strong></a>
  <br/>
</p>

<br/>


<h3 id="authors-and-copyright" align="center"><br/>✏️  Authors and Copyright  ✏️</h3>

<p align="center">
  👨🏽‍💻: <strong>Pietrobon Andrea</strong>
  <br/>
  🌐: 
  <a href="https://www.pietrobonandrea.com">pietrobonandrea.com</a>
  <br/>
  <img src="https://assets.stickpng.com/thumbs/580b57fcd9996e24bc43c53e.png" width="30" height="30" align="center">:
  <a href="https://twitter.com/pietrobonandrea">@PietrobonAndrea</a>
  <br/>
  🗄:
  <a href="https://github.com/Piero24/twitch-stream-viewer">twitch-stream-viewer</a>
  <br/>
  <br/>
  <br/>
  My name is <strong>Pietrobon Andrea</strong>,
  <br/>
  a computer engineering student at the 
  <br/>
  <img src="https://upload.wikimedia.org/wikipedia/it/thumb/5/53/Logo_Università_Padova.svg/800px-Logo_Università_Padova.svg.png"  width="30" height="30" align="center"> University of Padua (🇮🇹).
  <br/>
  <br/>
  My passion turns towards <strong>AI</strong> and <strong>ML</strong>.
  <br/>
  I have learned and worked in different sectors that have allowed me to gain skills 
  <br/>
  in different fields, such as IT and industrial design.
  <br/>
  <br/>
  To find out more, visit my 
  <br/>
  <a href="https://github.com/Piero24/Template-README/blob/main/LICENSE"><strong>website »</strong></a>
  <br/>
  <br/>
  The license of this repo as indicated in the 
  <a href="#general-license">general license</a> section is the 
  <br/>
  GNU General Public License v3.0
  <br/>
  For more details visit the 
  <a href="https://github.com/Piero24/Template-README/blob/main/LICENSE"><strong>licensing page »</strong></a>
  <br/>
  <br/>
  <strong>The Copyright (C) of this project is held exclusively by my person.</strong>
</p>

<p align="right"><a href="#top">⇧</a></p>

---
<br/>

> *<p align="center"> Copyrright (C) by Pietrobon Andrea <br/> Released date: Nov-2022*
