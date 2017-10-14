###Copy and clean the HTML first. Beautiful Soup will return nothing if you scrape using the URL if the site does not have perfectly formed html.###

###Download BeautifulSoup first. Use python3.6.3 as many built-ins are reformed that would be used , e.g. urllib2 is now just urllib###

###import BeautifulSoup from bs4###
from bs4 import BeautifulSoup

###define a variable that will take the place of the html in BeautifulSoup parser later###
sitetext = """
###Insert uncleaned html here. Save webpage as html; open with an editor like emacs or sublime text to wrap in this code###
"""
###the 'html.parser' code is present even though BeautifulSoup calls it as the default. If unadded, you get a warning in IDLE.###
###prettify does a good job aligning and cleaning html.###
soup = BeautifulSoup(sitetext, 'html.parser')
print(soup.prettify())

###Copy the output and use it in the cleanhtmlScrape python file###
