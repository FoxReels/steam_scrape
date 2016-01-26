from sys import argv
import re
import mechanize
from BeautifulSoup import BeautifulSoup

script, steam = argv

def scrape_profile(steam_profile_name):
	steam_profile_url = "http://steamcommunity.com/id/" + str(steam_profile_name) + "/games/?tab=all" #generate Steam profile url
	br = mechanize.Browser()
	html = br.open(steam_profile_url) #open browser to profile url
	soup = BeautifulSoup(html) #put it in the soup
	p = re.compile(ur'"appid":(\d*)') #compile regex to find appids
	appids = re.findall(p, str(soup))
	print len(appids)
	
scrape_profile(steam)