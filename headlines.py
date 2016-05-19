
# -*- coding: utf-8 -*-

import feedparser
import os

from flask import Flask
from flask import render_template

tmpl_dir = os.path.joihn(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)

RSS_FEEDS = { 'cc': 'http://blog.cheapcaribbean.com/rss',
              'applevac': 'http://www.applevacationsblog.com/feed/',
              'travelpulse': 'http://www.travelpulse.com/rss/news.rss?category=5123',
              'skift': 'https://skift.com/feed/'}

CC_FEED = "http://blog.cheapcaribbean.com/rss"

@app.route("/")
@app.route("/<publication>")

def get_news(publication="cc"):
    feed = feedparser.parse(RSS_FEEDS[publication])
    # for article in feed['entries']:

    # first_article = feed['entries'][0]
    # title = first_article.get("title")
    # published = first_article.get("published")
    # summary = first_article.get("summary").replace(u"\u2018","'").replace(u"\u2019", "'")

    return render_template("home.html", articles=feed['entries'])

    #"""<html><body style="background-image:url(http://cdn1.sciencefiction.com/wp-content/uploads/2014/03/sailor_moon_by_anouet-d5e58cu.png);"><h1> CC Blog Feed</h1><div style='display:block;'><a href="/cc">CheapCaribbean.com Blog</a><a href="/travelpulse">Travel Pulse Blog</a><a href="/applevac">Apple Vacations Blog</a><a href="/skift">Skift Blog</a></div><b>{0}</b><br/><i>{1}</i><br/><p>{2}</p><br/></body></html>""".format(title, published, summary)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
