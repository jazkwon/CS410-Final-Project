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
    :return:  Event List
    Loads Events from json file
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
    query_words = search_query.split()
    new_query = [word for word in query_words if word not in stopwords.words('english')]
    return new_query

def score_event(event, query):
    score = 0
    event_stuff = [event.title.split(), event.type.split(), event.sponsor.split(), event.location.split(),
                   event.date_time.split(), event.details.split()]
    for thing in event_stuff:
        for event_word in thing:
            for query_word in query:
                if event_word == query_word:
                    score += 1
    return score

def get_all_event_scores(events_list, search_query):
    events_score_list = []
    new_query = remove_stop_words(search_query)
    for event in events_list:
        events_score_list.append(score_event(event, new_query))
    return events_score_list

def write_top_events_to_string_list(ranked_events, num_events):
    ranked_events.reverse()
    event_strings = []
    for event in ranked_events[0:num_events]:
        event_strings.append(event.event_to_string())
    return event_strings

def write_list_to_file(string_list):
    file = open('top_events.txt', 'w')
    for event in string_list:
        file.write("%s\n" % event)
        file.write("\n###\n\n")
    
if __name__ == '__main__':
    events_list = load()
    events_scores = get_all_event_scores(events_list, "Computer Science Lecture")
#     print(events_list)
    ranked_events = [x for _,x in sorted(zip(events_scores,events_list))]
    write_list_to_file(write_top_events_to_string_list(ranked_events, 5))
#     print(events_scores)
#     print(events_list[events_scores.index(8)])
#     print(ranked_events)