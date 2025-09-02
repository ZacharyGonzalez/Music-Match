
import json
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import json
from data_services import DataServices

songs = {}
options = Options()
profile_path = "/home/zack-gonzalez/.mozilla/firefox/sjhpz778.default-release"
profile = FirefoxProfile(profile_path)
options.profile = profile
driver = webdriver.Firefox(options=options)
ds = DataServices()

# i havent included cities with a space in their name like 'Las Vegas'
locations = 'Anaheim Antlanta Austin Charlotte Chicago Cleveland DAllas Denver Detroit Houston Indianapolis Memphis Miami Minneapolis Nashville New Orleans New York City Omaha Philadelphia Pheonix Pittsburgh Portland Sacramento Seattle Tampa Washington'.split(' ')
subset = locations[0:1] # i dont know if i can store every cities top 50 easily
week = 'test_week'
for city in subset:
    driver.get(f'https://charts.spotify.com/charts/view/citytoptrack-{city}-weekly/2025-08-28')
    time.sleep(7) 
    table_rows = driver.find_elements(By.XPATH, "/html/body/div[1]/div/div[3]/div/table/tbody/tr")
    current_song = ''
    for row in table_rows:
            try:
                href_links = row.find_elements(By.TAG_NAME,"a")
                for link in href_links:
                    href = link.get_attribute("href")
                    if href: 
                        if 'track' in href:
                            current_song = href
                            songs[href] = []  
                        if 'artist' in href:
                            songs[current_song].append(href)

            except Exception as e:
                print(f"Error processing row: {e}")
    city_songs = [week, city, songs]
    ds.chart_data_processing(city_songs)

driver.quit()