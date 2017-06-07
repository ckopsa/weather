#!/usr/local/bin/python3
import requests, bs4, sys, os

weatherFilePath = os.getcwd() + "/weather.txt"
url = "https://weather.com/weather/today/l/"
zip = sys.argv[1]
ext = ":4:US"
res = requests.get(url + zip + ext)
res.raise_for_status();
weatherSoup = bs4.BeautifulSoup(res.text, "html.parser")
weatherCard = weatherSoup.find("div", { "class" : "today_nowcard-temp" })
weatherFile = open(weatherFilePath, 'r+')
if weatherCard is not None:
    temp = weatherCard.select('span')[0].getText()
    weather = weatherSoup.find("div", { "class" : "today_nowcard-phrase" }).getText()
    weatherTemp = temp + ' ' + weather
    weatherFile.seek(0)
    weatherFile.truncate()
    weatherFile.write(weatherTemp)
    print(weatherTemp)
else:
    print (weatherFile.readline())
weatherFile.close()
