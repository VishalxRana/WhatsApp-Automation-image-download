from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
#import pywhatkit

PATH = "C:\chromedriver.exe" #Path to where the chromedriver is saved 
driver = webdriver.Chrome(PATH)
driver.get("https://web.whatsapp.com/")

time.sleep(10)

def download_img():
    # searches the name of the user. Then you have to manually click and open it. 
    search = driver.find_element_by_xpath("Enter XPATH of the search field")
    search.send_keys("Enter User name")

    time.sleep(5)

    #opens the header area. Area at the top where name is written and DP is there.
    header = driver.find_element_by_xpath("Enter XPATH of the header region")
    header.click() 

    time.sleep(3) 

    #opens the images folder. Here all images can be seen 
    folder = driver.find_element_by_xpath("Enter XPATH of the folder region")
    folder.click()

    time.sleep(3)

    #Once the folder is opened. The first image from the folder is later opened
    img = driver.find_element_by_xpath("Enter XPATH of the first image")
    img.click()

    for images in range(0, 59): # Enter the number of images to be downloaded instead of 59
        time.sleep(2)

        # downloads the image 
        download = driver.find_element_by_xpath("Enter XPATH of the download botton")
        download.click()

        time.sleep(1)

        #clicks the previous arrow button so the previous image is shown.
        prev = driver.find_element_by_xpath("Enter XPATH of the left button")
        prev.click()

download_img()
