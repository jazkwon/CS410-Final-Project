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
        :param date: Event date
        :param time: Event time
        :param details: Event details
        """
        self.title = title
        self.type = type
        self.sponsor = sponsor
        self.location = location
        self.date_time = date_time
        self.details = details
