import time
import os
import datetime
from selenium import webdriver
import webbrowser
import urllib



def debianScreenGrab(url, user):
    todayDate = time.strftime("%m-%d-%y")
    directory = os.getcwd() + '/Records/ScreenShots/%s/%s' % (todayDate, user)
    if not os.path.exists(directory):
        os.makedirs(directory)
    fileSystime = datetime.datetime.strftime(datetime.datetime.now(), '%H_%M_%S')
    imageName = str('%s/%s_%s.png') % (directory, user, fileSystime)

    try:
        browser = webdriver.Firefox()
        browser.get(url)
        time.sleep(5)
        browser.save_screenshot(imageName)
        browser.quit()
    except:
        print "\n [!] ERROR: Debian Screenshot Error\n"


def tweetHTMLGrab(url, user):
    todayDate = time.strftime("%m-%d-%y")
    directory = os.getcwd() + '/Records/HTML/%s/%s' % (todayDate, user)
    if not os.path.exists(directory):
        os.makedirs(directory)
    fileSystime = datetime.datetime.strftime(datetime.datetime.now(), '%H_%M_%S')
    fileName = str('%s/%s_%s.html') % (directory, user, fileSystime)

    browser = 'google-chrome'
    webbrowser.get(browser).open_new_tab(url)
    page = urllib.urlopen(url)

    webContent = page.read()
    f = open(fileName, 'w')
    f.write(webContent)
    f.close()


def main(data, os):

    url = "https://twitter.com/%s/status/%s" % (str(data['user']['screen_name']), str(data['id']))
    user = str(data['user']['screen_name'])

    try:

        if os == 'Linux':
            debianScreenGrab(url, user)

    except:
        print '[!] Error Getting or Saving Screenshot'