import urllib,urllib2
import downloader
import json
import webbrowser
from BeautifulSoup import BeautifulSoup

class Reddit:
    base_urlreddit="https://api.imgur.com/3/gallery/r/"

    def __init__(self,client_id,subreddit):
        self.client_id=client_id
        self.subreddit=subreddit
        self.pic_list=[]

    def get_gallery(self):
        urlreddit=self.base_urlreddit+self.subreddit
        opener = urllib2.build_opener()
        opener.addheaders = [('Authorization', 'Client-ID '+self.client_id)]
        try:
            response=opener.open(urlreddit)
            js=json.loads(response.read())
            for data in js['data']:
                if "link" in data:
                    self.pic_list.append(data["link"])
        except Exception as e:
            print "Error"
            print e
            pass
        return self.pic_list

