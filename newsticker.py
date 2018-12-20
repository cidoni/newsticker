# THIS SCRIPT USES THE LIBRARY AT:
# https://github.com/hzeller/rpi-rgb-led-matrix

import os, time, threading, random
import feedparser
import re
from random import shuffle

BITLY_ACCESS_TOKEN="BITLY_ACCESS_TOKEN"
items=[]
displayItems=[]
feeds=[
    #enter all news feeds you want here
    "http://feeds.bbci.co.uk/news/world/rss.xml"
    #"http://feeds.reuters.com/reuters/topNews",
    #"https://www.npr.org/rss/rss.php?id=1001",
    #"http://feeds.feedburner.com/ndtvnews-latest"
    #"https://markets.businessinsider.com/rss/news",
    #"https://www.cio.com/index.rss"
    ]

def colorRandom():
    return str(random.randint(0,255)) + "," + str(random.randint(0,255))  + "," + str(random.randint(0,255))

def populateItems():
    #first clear out everything
    del items[:]
    del displayItems[:]

    for url in feeds:
        feed=feedparser.parse(url)
        items.append("\*\*\* " + feed["feed"]["title"] + " \*\*\* \n")
        print(feed["feed"]["title"]) 
        posts=feed["items"]
        for post in posts:
            items.append(post["title"]+": "+post["summary"]+" \n")
    #shuffle(items)

def run():
    print("News Fetched at {}\n".format(time.ctime()))
    populateItems()
    threading.Timer(len(items) * 60, run).start()
    showOnLEDDisplay()

def showOnLEDDisplay():
    for disp in items[:60]:
        txt=re.sub("'","\\'",disp)
        print (disp)
        os.system("sudo /home/pi/risrim/display16x32/rpi-rgb-led-matrix/examples-api-use/scrolling-text-example --led-rows=16 --led-cols=32 -f /home/pi/risrim/display16x32/rpi-rgb-led-matrix/fonts/7x14.bdf -s 10 -C "+ colorRandom() +" -b 50 -l 1 "+txt)

if __name__ == '__main__':
    run()
