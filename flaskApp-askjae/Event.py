'''
Created on May 9, 2018

@author: andrewbloomberg
'''


class Event(object):
    '''
    This class stores the data for Event
    '''

    def __init__(self, title, type, sponsor, location, date_time, details):
        """
        :param title: Event title
        :param type: Event type
        :param sponsor: Event sponsor
        :param location: Event location
        :param date_time: Event date and time
        :param details: Event details
        """
        self.title = title.encode('ascii','ignore')
        self.type = type.encode('ascii','ignore')
        self.sponsor = sponsor.encode('ascii','ignore')
        self.location = location.encode('ascii','ignore')
        self.date_time = date_time.encode('ascii','ignore')
        self.details = details.encode('ascii','ignore')
        
    def event_to_string(self):
        """
        :return:  The event in a formatted string form
        Takes the event and puts all its parts together into a formatted string for use in displaying data on the website
        """
        event_string = ("Title:  " + str(self.title) + "\nType:  " + str(self.type) + "\nSponsor:  " + str(self.sponsor) + 
        "\nLocation:  " + str(self.location) + "\nDate and Time:  " + str(self.date_time) + "\nDetails:  " + str(self.details) + "\n")
        return event_string
