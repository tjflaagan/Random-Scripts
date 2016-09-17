import urllib2
import urlparse
import os

os.system('cls' if os.name == 'nt' else 'clear')
Address = "http://www.dsu.edu"


Request = urllib2.Request(Address)

Request.add_header("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/600.3.18 (KHTML, like Gecko) Version/8.0.3 Safari/600.3.18")

Page = urllib2.urlopen(Request)

HTML = Page.read()

for Item in HTML.split("\n"):
    if "img" in Item:
        Image = Item.split("src=\"")[1].split("\"")[0]
        os.system("wget " + urlparse.urljoin(Address, Image))
        print Image