###See comments about BeautifulSoup and python3.6.3 from cleanHTML.py###

from bs4 import BeautifulSoup

siteHTML = """
###Use cleaned HTML from cleanhtml.py program. This program can take thousands of lines of html and still print results fast.###
"""

###It is necessary to write a function if the text you want to scrape falls within deeper tags or specific css class. 
###Replace CLASSTYPE with the name of the css class. This will be a different identifier for most sites, so you have to use that specific term.###
###Note that 'div' is used, but this could also be a 'tr' or other tag that designates physical location. CSS class identifies the specific text within that div you want to scrape.###
soup = BeautifulSoup(siteHTML, "html.parser")
for products in soup.find_all('div', attrs={"class" : "CLASSTYPE"}):
    print (products.text)
  
###This will print out the text inline in your IDLE with a few breaks in between each term.###
###Future goal is to write more code that will allow for scraping specific data or text within different pages on the same site.##
