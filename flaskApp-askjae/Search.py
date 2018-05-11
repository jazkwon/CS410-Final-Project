'''
Created on May 9, 2018

@author: andrewbloomberg

This is the main class that runs the program
'''
from Event import Event
import json
from nltk.corpus import stopwords
import nltk
from posix import remove
nltk.download('stopwords')

def load():
    """
    :return:  List of event objects
    Loads Events from json file and puts the data into an event object
    """
    
    list_of_events = []
    
    with open('data.json') as infile:
        stored_data = json.load(infile)
        for thing in stored_data:
            data = stored_data[thing]
            for event in data:
                title = event['title']
                type = event["type"]
                sponsor = event["sponsor"]
                location = event["location"]
                date_time = event["date"] + " " + event["time"]
                details = event["details"]
                list_of_events.append(Event(title, type, sponsor, location, date_time, details))
    
    with open('data2.json') as infile:
        stored_data = json.load(infile)
        for event in stored_data:
            title = event['Title']
            type = event["Event Type"]
            sponsor = event["Sponsor"]
            location = event["Location"]
            date_time = event["Date "]
            details = event["Description"]
            list_of_events.append(Event(title, type, sponsor, location, date_time, details))
    return list_of_events

def remove_stop_words(search_query):
    """
    :param search_query:  The raw text of the query typed in by the user
    :return:  The text from the search bar with the stop words removed
    Removes all stop words from the search query typed in by the user
    """
    query_words = search_query.split()
    new_query = [word for word in query_words if word not in stopwords.words('english')]
    return new_query

def score_event(event, query):
    """
    :param event:  Event Object
    :param query:  Edited search query broken up into a list of words from the query
    :return:  The score of the event based on the search query
    Scores each event based on the modified search query.  Simple scoring function giving a point for each time a word in the
    query appears in any of the section of the event data.
    """
    score = 0
    event_stuff = [event.title.split(), event.type.split(), event.sponsor.split(), event.location.split(),
                   event.date_time.split(), event.details.split()]
    for thing in event_stuff:
        for event_word in thing:
            for query_word in query:
                if event_word.lower() == query_word.lower():
                    score += 1
    return score

def get_all_event_scores(events_list, search_query):
    """
    :param events_list:  List of events
    :param search_query:  The modified search query
    :return:  A list of scores corresponding to the each event in the event list
    Scores every event based on the search query
    """
    events_score_list = []
    new_query = remove_stop_words(search_query)
    for event in events_list:
        events_score_list.append(score_event(event, new_query))
    return events_score_list

def write_top_events_to_string_list(ranked_events, num_events):
    """
    :param ranked_events:  List of events from lowest score to highest score
    :param num_events:  Number of events to return
    :return:  List of events in string form
    Takes the top "num_events" ranked events from the list and returns a list of them each in a string format
    """
    ranked_events.reverse()
    event_strings = []
    for event in ranked_events[0:num_events]:
        event_strings.append(event.event_to_string())
    return event_strings

def write_list_to_string(string_list):
    """
    :param string_list:  List of events in string format
    :return:  One big string of all the events
    Takes all the events in string form and combines them into one big formatted string to be used when displaying text on
    the web page.
    """
    event_string = ""
    for event in string_list:
        event_string += event + "\n###\n\n"
    return event_string
        
def write_top_results_to_string(search_query):
    """
    :param search_query:  The raw search query
    :return:  One big string of events
    Does all the steps starting with the raw search query and end with returning the big string of events for posting on
    web page
    """
    events_list = load()
    events_scores = get_all_event_scores(events_list, search_query)
    tuple_list = []
    for i in range(0, len(events_list)):
        tuple_list.append((events_scores[i], events_list[i]))
#     ranked_events = [x for _,x in sorted(zip(events_scores,events_list))]
    tuple_list.sort()
    ranked_events = []
    for event in tuple_list:
        ranked_events.append(event[1])
    return write_list_to_string(write_top_events_to_string_list(ranked_events, 5))
    
def write_events_by_tag_to_string(tag):
    """
    :param tag:  A tag in string form
    :return:  A big string of all the events that relate to this tag
    Takes in a tag/filter selected on the web site and finds all events in the database that mention that tag.  It compiles
    all these events, and returns them in a giant formatted string for displaying on the web page.
    """
    events_list = load()
    tagged_event_strings = []
    for event in events_list:
        event_string = event.event_to_string()
        if tag.lower() in event_string.lower():
            tagged_event_strings.append(event_string)
    return write_list_to_string(tagged_event_strings)
    
if __name__ == '__main__':
    print(write_top_results_to_string("Lecture"))
#     print(write_events_by_tag_to_string("Lecture")) 
    
#     events_list = load()
#     events_scores = get_all_event_scores(events_list, "Computer Science Lecture")
#     print(events_list)
#     ranked_events = [x for _,x in sorted(zip(events_scores,events_list))]
#     write_list_to_file(write_top_events_to_string_list(ranked_events, 5))
#     print(events_scores)
#     print(events_list[events_scores.index(8)])
#     print(ranked_events)