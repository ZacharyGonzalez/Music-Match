
import json
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import json

elems={}
cities={}
weeks={}
options=Options()
profile_path = "/home/zack-gonzalez/.mozilla/firefox/sjhpz778.default-release"
profile = FirefoxProfile(profile_path)
options.profile=profile
driver = webdriver.Firefox(options=options)

# i havent included cities with a space in their name like 'Las Vegas'
locations='Anaheim Antlanta Austin Charlotte Chicago Cleveland DAllas Denver Detroit Houston Indianapolis Memphis Miami Minneapolis Nashville New Orleans New York City Omaha Philadelphia Pheonix Pittsburgh Portland Sacramento Seattle Tampa Washington'.split(' ')
subset=locations[0:1] # i dont know if i can store every cities top 50 easily
weeks['date'] = []
for city in subset:
    driver.get(f'https://charts.spotify.com/charts/view/citytoptrack-{city}-weekly/2025-08-28')
    time.sleep(7)
    rows = driver.find_elements(By.XPATH, "/html/body/div[1]/div/div[3]/div/table/tbody/tr")
    song = ''
    for row in rows:
            try:
                links = row.find_elements(By.TAG_NAME,"a")
                for link in links:
                    href = link.get_attribute("href")
                    if href:
                        if 'track' in href:
                            song=href
                            elems[href] = []
                        if 'artist' in href and song:
                            elems[song].append(href)
            except Exception as e:
                print(f"Error processing row: {e}")
    cities[city] = elems
weeks['date'] = cities
with open('./docs/test.txt','w+') as o:
    json.dump(weeks,o)
driver.quit()