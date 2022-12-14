import requests
from bs4 import BeautifulSoup

url = "https://www.ultimate-guitar.com/explore"
url_result = requests.get(url).text
html_doc = BeautifulSoup(url_result, "html.parser")

tag = html_doc.find("div", class_="js-store")
mumblejumble = tag["data-content"]
mumblejumble_split = mumblejumble.split(",")

start_string = "tab_url"

uncleaned_link_list = []

# Produce a list where each element in the list is a string à la "tab_url":"https://tabs.ultimate-guitar.com/..."
uncleaned_link_list = [element for element in mumblejumble_split if element.startswith('"tab_url"')]

# Clean the list by stripping away the "tab_url":

cleaned_link_list = [element.split(':')[2].strip('"').strip('"//') for element in uncleaned_link_list]



for element in cleaned_link_list:
    print(element)





