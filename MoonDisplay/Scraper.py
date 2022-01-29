import os

try:
    from bs4 import BeautifulSoup
except:
    try:
        os.system("pip install beautifulsoup4")
    except:
        print("Couldn't install bs4")

try:
    import requests
except:
    try:
        os.system("pip install requests")
    except:
        print("Couldn't install requests")

import re

imagePath = os.path.dirname(os.path.realpath(__file__)) + "\\Images\\"



def handleLunarData():
    moonSite = "https://www.calendarr.com/united-states/moon-today/"
    moonContent = requests.get(moonSite).text
    moonSoup = BeautifulSoup(moonContent, 'lxml')
    moonPhaseImg = moonSoup.find_all("img")[1]['src']
    moonPhaseTxt = moonSoup.find_all("h3")[0].text
    with open(imagePath + "moonPhase.jpg", "wb") as f:
        f.write(requests.get(moonPhaseImg).content)
    return moonPhaseTxt

def handleWeatherData():
    weatherSite = "https://forecast.weather.gov/MapClick.php?CityName=Bethesda&state=MD&site=LWX&lat=38.9898&lon=-77.1203"
    weatherContent = requests.get(weatherSite).text
    weatherSoup = BeautifulSoup(weatherContent, 'lxml')
    weatherConditionImg = ''
    weatherConditionTxt = ''
    for img in weatherSoup.find_all("img"):
        if "tonight" in str(img).lower():
            weatherConditionImg = "https://forecast.weather.gov/" + img['src']
    lockA = False
    lockB = False
    for p in weatherSoup.find_all("p"):
        if "current-lrg" in str(p).lower() and not lockA:
            currentTemperature = p.text
            lockA = not lockA
        if "short-desc" in str(p).lower() and not lockB:
            weatherConditionTxt = re.findall(r"<p class=\".*\">(.*)<\/p>", str(p))[0].replace("<br/>", " ")
            lockB = not lockB
    with open(imagePath + "weatherImg.png", "wb") as f:
        f.write(requests.get(weatherConditionImg).content)
    return (weatherConditionTxt, currentTemperature)

handleWeatherData()