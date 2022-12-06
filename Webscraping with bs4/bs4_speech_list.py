from bs4 import BeautifulSoup
import re
import requests

# HTML From File
with open("cbspeeches from BIS site.htm", "r") as f:
	doc = BeautifulSoup(f, "html.parser")


title_tags = doc.find_all(class_="title") # To extract the tag of the class title

speech_title = []

for title_tag in title_tags:
	a_tag = title_tag.find("a") # To extract a tag within a tag, i.e. the a tag within the above tag
	#print(a_tag.contents[0])
	speech_title.append(a_tag.contents[0])

print(speech_title)













