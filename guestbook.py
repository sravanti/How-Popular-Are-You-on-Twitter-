__author__ = 'sravantitekumalla'
import os
import cgi
import urllib

from twitterAuth import twitterAuth

import jinja2
import webapp2



JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)




class MainPage(webapp2.RequestHandler):

    def get(self):




        template_values = {


        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))


class Guestbook(webapp2.RequestHandler):

    def post(self):
        name = self.request.get('content')
        f = twitterAuth(name)
        numFollowers = f.getFollowers()
        numTweets = f.getTweets()
        avgFavs = f.getAverageFavs()
        avgRTs = f.getAverageRTs()
        friendRatio = f.getFriendRatio()
        numMentions = f.getMentions()
        name = f.getName()
        popsum = f.popularity()

        template_values = {

            'numFollowers': numFollowers,
            'numTweets': numTweets,
            'avgFavs': avgFavs,
            'avgRTs' : avgRTs,
            'friendRatio': friendRatio,
            'numMentions': numMentions,
            'name': name,
            'popsum': popsum
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', Guestbook),
], debug=True)