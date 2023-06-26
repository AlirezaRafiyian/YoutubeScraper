from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

# Set up the Selenium driver
driver = webdriver.Chrome()

# Channel URL you want to scrap videos from it
channel_url = 'https://www.youtube.com/@BeInspiredChannel/videos'
driver.get(channel_url)

# Wait for the page to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#video-title')))


# Scroll down the page to load more videos
scrollPauseTime = 4 # as needed
scrollHeight = driver.execute_script("return document.documentElement.scrollHeight")

while True:
    # Scroll to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")

    # Wait for the videos to load
    driver.implicitly_wait(scrollPauseTime)

    # Calculate the new scroll height
    newScrollHeight = driver.execute_script("return document.documentElement.scrollHeight")

    # Checking if the page has reached to the end
    if newScrollHeight == scrollHeight:
        break

    # Update the scroll height
    scrollHeight = newScrollHeight

# Extracting the video labels and links
videoElements = driver.find_elements(By.CSS_SELECTOR, '#video-title')
videoInfo = {}

for element in videoElements:
    label = element.text.strip()
    link = element.get_attribute('href')
    videoInfo[label] = link

for i, label in enumerate(videoInfo, start=1):
    print(f'{i}. {label}')

selectedVideo = int(input("Enter the number of the video you want to watch: "))

# Check if the selected video number is within the valid range
if 1 <= selectedVideo <= len(videoElements):
    # Open the selecetd video in the browser
    videoElements[selectedVideo - 1].click()
else:
    print("Invalid video number.")

quitChrome = int(input("If you want to quit just enter the zero "))
if quitChrome == 0:
    driver.quit()
