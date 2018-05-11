# CS410-Final-Project
echen35, jhkwon3, bloombe2

## Code Overview

### Web Scraper
  <p>These python scripts scrape predetermined UIUC Engineering webpages to pull calendar event data. The data includes event details such as title, type, date, time, location, host, and description. The data was then formatted and outputted to a JSON file. </p>

### Search Bar
  <p>
	The search bar allows the user to enter a query and receive the top five most related events to the query. This can be used for searching for UIUC Engineering events relating to a specific topic. Instead of visiting each site individually, the user can now browse all relevant events on one page.
	Similar to the ranking system we learned in class, we implemented our search bar to process the query and map the keywords to our collected data. The search function processes the query and assigns weights to the query words; the stop-words are weighted 0 and the keywords are weighted 1. Then, the weights for each event are summed, and the events with the top five greatest scores are pushed and populate the webpage.  We decided against using metapy and instead wrote our own search and parse algorithms.</p>

### Tags
  <p>
	The tag button under the search bar pulls down a selection of type buttons that allow the user to organize and view the events by type. Each type button pulls all events correlated to that button (i.e. the seminar button gets and posts all the events of type “seminar”).  We only implemented one variant of the tags function; in the future, different types of tags could be included as well. For example, we could add the ability to organize data by organization (i.e. a potential NCSA Events button could get and post all the NCSA events).
  </py>


Note: see code for detailed documentation on software functions and implementation

## How to use the Software

### Setup
```
	1. Clone the repo from our github and navigate to the folder in your terminal
	2. Check your python version (type the command python --version)
		a. Be sure you are using Python 2.7 (Preferrably 2.7.5 if possible)
		b. If you do not have Python 2.7 installed…
			i. Download Python 2.7 as instructed here
			ii. In the terminal run <code>curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py </code>
			ii. In terminal, run the command  <code> sudo python get-pip.py</code>
	3. Navigate to the /flaskApp-askjae folder in the terminal
	4. If Flask is not installed on your machine, run the command <code>sudo pip install flask</code>
	5. Use Python 2.7 to run python app.py
		a. Note: Be sure you are in the same directory as the app.py file
	6. Copy the local host address (http://127.0.0.1:5000/) into your web browser

	Note: We tried running this on Python3, but for some reason, we could not build the project

```

### Using the Website
```
	1. Type search query in search bar (key words, event type ... ) and press the search button
		a. Events matching the query should populate the page.
	2. Click on the Tags button to view the tags for the events
		a. Select a tag and all the events with a matching type should populate the page
```


Team Member Contributions

Jasmine  
	Scraped and stored data in JSON about NCSA and General Campus Events. Merged frontend with backend.

Emily
	Coded up the front end of the website.  Merged frontend with backend.

Andrew  
	Scraped and stored data in JSON about CS and ECE events on campus.  Wrote the search function

All together  
	Came up with designs, concepts, and ideas for website
