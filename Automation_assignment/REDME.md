
## Requirements:

1. Python
2. Selenium
3. Chromedriver

## Precedure:

### First, install Google Chrome for Debian/Ubuntu:

>> sudo apt-get install libxss1 libappindicator1 libindicator7
>> wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

>> sudo dpkg -i google-chrome*.deb
>> sudo apt-get install -f

## Now, let’s install xvfb so we can run Chrome headlessly:

>> sudo apt-get install xvfb

## Install ChromeDriver:

>> sudo apt-get install unzip

>> wget -N http://chromedriver.storage.googleapis.com/2.26/chromedriver_linux64.zip
>> unzip chromedriver_linux64.zip
>> chmod +x chromedriver

>> sudo mv -f chromedriver /usr/local/share/chromedriver
>> sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
>> sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver

## Install some Python dependencies and Selenium:

# Install pip:
>> sudo apt-get install python-pip

# Install Selenium :
>> sudo python -m pip install selenium

<!-- Follow this link for REF.
https://christopher.su/2015/selenium-chromedriver-ubuntu/ -->

## To run the .py automation file :

### Command:
>> python browser_automation.py
