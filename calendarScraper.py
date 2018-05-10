import urllib
import urllib.request
import logging
import json

from bs4 import BeautifulSoup

dates = []
linkExtensions = []
base_url = 'https://calendars.illinois.edu'
event_tags = []
event_info = []
events_dict = []

def scrapeCalendar(url):
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    calendarMainContent = soup.find("div", {"class": "place-on-screen"})
    for date in calendarMainContent.find_all("h2"):
        dates.append(date.text)
    for events in calendarMainContent.find_all("ul", {"class": "event-entries"}):
        #print(events.prettify())
        for title in events.find_all("div", {"class": "title"}):
            for link in title.find_all('a', href=True):
                linkExtensions.append(link['href'])
                #print(link['href'])
    for i in range(len(linkExtensions)):
        events_dict.append(getEventInfo(base_url + linkExtensions[i]))
    with open('data2.txt', 'w') as outfile:
        json.dump(events_dict, outfile, indent=4)

def getEventInfo(link):
    page = urllib.request.urlopen(link)
    soup = BeautifulSoup(page, "html.parser")
    title = soup.find("h2", {"id": "ws-title"}).text
    event_tags.append("Title")
    event_info.append(title)
    eventContent = soup.find("dl")
    for types in eventContent.find_all("dt"):
        event_tags.append(types.text)
    event_tags.append("Description")
    for info in eventContent.find_all("dd"):
        event_info.append(info.text)

    #print(len(event_tags))
    #print(len(event_info))
    eventInfoDictionary = dict(zip(event_tags, event_info))
    return(eventInfoDictionary)

if __name__ == '__main__':
    scrapeCalendar('https://calendars.illinois.edu/list/772')
