'''
Created on May 9, 2018

@author: andrewbloomberg

This is the main class that runs the program
'''
from bs4 import BeautifulSoup
from Event import Event
import json
import urllib2
import re
from urllib2 import URLError
import json
from __builtin__ import IndexError

event_object_list = []
ece_event_link_list = []

def scrape_ece_event_links(url):
    """
    :param url: url of calendar page
    Scrapes all the links from the ECE calendar page
    """
    header = {'User-Agent': 'Mozilla/5.0'}
    req = urllib2.Request(url, headers=header)
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page)
    content = soup.findAll("a")
    events = []
    for link in content:
        if "calendar/event" in str(link.get("href")):
            ece_event_link_list.append("ece.illinois.edu" + str(link.get('href')))
            
def ece_event_link_to_object(url):
    """
    :param url: url of ECE event page
    Turns ECE event link into event object
    """ 
    try:
        header = {'User-Agent': 'Mozilla/5.0'}
        req = urllib2.Request("http://" + url, headers=header)
        page = urllib2.urlopen(req)
        soup = BeautifulSoup(page)
        content = soup.find("div", {"class": "section grey"})
        title = content.findAll("h2")[1].text
        table = content.find("table").findAll(text = True)
#         print(table)
        
        type = table[40]
        sponsor = table[34]
        location = table[28]
        date = table[16]
        time = table[22]
        try:
            details = " ".join(table[46:])
        except AttributeError:
            return
    except IndexError:
        print("Whoops")
        return
    event = Event(title, type, sponsor, location, date, time, details)
    event_object_list.append(event)
#     print(title)
#     print(type)
#     print(sponsor)
#     print(location)
#     print(date)
#     print(time)
#     print(details)

def scrape_cs_event_links(url):
    """
    :param url: url of calendar page
    Scrapes all the links from the CS calendar page
    """
    header = {'User-Agent': 'Mozilla/5.0'}
    req = urllib2.Request(url, headers=header)
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page)
    content = soup.find_all("a")
    events = []
    for link in content:
        if "eventId" in str(link.get("href")):
            events.append("calendars.illinois.edu" + str(link.get('href')))
    events = set(events)
    events = list(events)
    return(events)

def cs_event_link_to_object(url):
    """
    :param url: url of CS event page
    Turns CS event link into event object
    """ 
    try:
        header = {'User-Agent': 'Mozilla/5.0'}
        req = urllib2.Request("http://" + url, headers=header)
        page = urllib2.urlopen(req)
        soup = BeautifulSoup(page)
        content = soup.find("section", {"class": "detail-content"})
        title = content.find("h2").text
        type = content.find("a").text
        list_of_things = content.findAll("dd")
        sponsor = list_of_things[1].text
        location = list_of_things[2].text
        date_time = list_of_things[3].text
        date = " ".join(date_time.split()[0:3])
        time = " ".join(date_time.split()[3:])
        try:
            details = " ".join(content.find("dd", {"class":"ws-description"}).findAll(text=True))
        except AttributeError:
            return
    except IndexError:
        print("Whoops")
        return
    event = Event(title, type, sponsor, location, date, time, details)
    event_object_list.append(event)
#     print(title)
#     print(type)
#     print(sponsor)
#     print(location)
#     print(date_time)
#     print(date)
#     print(time)
#     print(details)
#     print(list_of_things)


def store():
    """
    Stores data to a json file
    """
    to_save = {'events': []}
    for event in event_object_list:
        to_save['events'].append(
            {'title': event.title, 'type': event.type, 'sponsor': event.sponsor, 'location': event.location, 'date': event.date,
             'time': event.time, 'details': event.details})

    with open('data.json', 'w') as outfile:
        json.dump(to_save, outfile, indent=4, sort_keys=True)


if __name__ == '__main__':
    scrape_ece_event_links("https://ece.illinois.edu/calendar/week/5/9/2018")
    scrape_ece_event_links("https://ece.illinois.edu/calendar/week/5/16/2018")
    for event in ece_event_link_list:
        ece_event_link_to_object(event)
    cs_events = scrape_cs_event_links("http://illinois.edu/calendar/list/2654")
    for event in cs_events:
        cs_event_link_to_object(event)
    store()
#     print(event_link_list)